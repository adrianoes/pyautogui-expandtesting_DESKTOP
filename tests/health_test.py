import time
import pyautogui
import os
import json
import subprocess

def test_health_curl():
    # Start video recording for this specific test
    ffmpeg_process, video_filename = start_video_recording("test_health_curl")
    
    # Starting the display
    os.environ["DISPLAY"] = ":99"
    
    starting_terminal()

    # Check if there is already an active capture script (avoids duplicate redirection)
    if not os.path.exists("/tmp/last"):
        print("Setting up terminal output capture...")
        # Redirect the output of the curl command directly to the /tmp/last file
        save_output_script = """curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json' > /tmp/last"""
        pyautogui.write(save_output_script, interval=0.1)
        pyautogui.press("enter")
        time.sleep(2)  # Wait more time to ensure the redirection is set up
    else:
        print("Output capture already set up. Skipping this step.")

    # Additional wait time to ensure the cURL command is processed
    time.sleep(10)  # Increase the wait time

    # Check the response in the /tmp/last file
    response_from_file = ""
    retry_count = 0
    max_retries = 10
    while retry_count < max_retries:
        if os.path.exists("/tmp/last") and os.path.getsize("/tmp/last") > 0:
            with open("/tmp/last", "r") as file:
                response_from_file = file.read().strip()
            if response_from_file:
                break  # Exit the loop as soon as content is found
        print(f"Attempt {retry_count + 1}: /tmp/last file still empty, waiting...")
        time.sleep(3)  # Increase the wait time between retries
        retry_count += 1
    print(f"Captured response: {response_from_file}")

    # If the response was captured, try to decode it in JSON
    passed = False
    if response_from_file:
        try:
            response_json = json.loads(response_from_file)
            success = response_json.get("success")
            status = response_json.get("status")
            message = response_json.get("message")
            print(f"Extracted data: success={success}, status={status}, message='{message}'")
            assert success == True, "Error: success is not True"
            assert status == 200, "Error: status is not 200"
            assert message == "Notes API is Running", "Error: incorrect message"
            print("✅ API health checks!")
            passed = True  # Test passed
        except json.JSONDecodeError:
            print("❌ Error converting the response to JSON!")
    else:
        print("❌ Response was not captured correctly.")

    # Close the terminal after capturing the response
    os.system("pkill xterm")

    # Stop video recording and decide what to do with the video
    stop_video_recording(ffmpeg_process, video_filename, passed)

def starting_terminal():
    # Check if the terminal is already open
    existing_process = os.popen("pgrep xterm").read().strip()    
    if not existing_process:
        print("Opening new xterm terminal...")
        os.system("xterm -fa 'Monospace' -fs 12 &")  # Forcing a default font to avoid errors
        time.sleep(5)  # Wait for the terminal to open
    else:
        print(f"xterm is already running (PID: {existing_process}). Not opening a new terminal.")
    time.sleep(2)    
    pyautogui.hotkey("alt", "tab")  # Ensure the terminal has focus
    time.sleep(1)

def start_video_recording(test_name):
    video_filename = f"/tmp/{test_name}_recording.mp4"
    ffmpeg_command = [
        "ffmpeg", "-y", "-f", "x11grab", "-video_size", "1920x1080", "-i", ":99", 
        "-r", "25", "-pix_fmt", "yuv420p", video_filename
    ]
    ffmpeg_process = subprocess.Popen(ffmpeg_command)
    print(f"Starting video recording for the test '{test_name}'...")
    return ffmpeg_process, video_filename

def stop_video_recording(ffmpeg_process, video_filename, passed):
    ffmpeg_process.terminate()  # Stop the video recording
    if passed:
        print(f"Test passed, deleting the video {video_filename}")
        os.remove(video_filename)  # Delete the video if the test passed
    else:
        print(f"Test failed, keeping the video {video_filename} as evidence.")
