import time
import pyautogui
import os
import json
import subprocess
import pyscreeze

def test_health_curl():
    # Start video recording for this specific test
    ffmpeg_process, video_filename = start_video_recording("test_health_curl")

    # Start display
    os.environ["DISPLAY"] = ":99"
    
    # Start terminal
    starting_terminal()

    # API Health Check
    print("Checking API health status...")
    
    save_output_script = """curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' \
    -H 'accept: application/json' \ > /tmp/last"""
    
    pyautogui.write(save_output_script, interval=0.1)
    
    # Ensure screenshot directory exists
    screenshot_dir = "reports/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    
    # Capture screenshot before execution
    screenshot_filename = f"reports/screenshots/test_health_curl_before_enter.png"
    pyautogui.screenshot(screenshot_filename)
    print(f"Screenshot saved at {screenshot_filename}")
    
    # Execute the command
    pyautogui.press("enter")
    
    # Wait for the response
    time.sleep(10)

    # Read the response from the file
    with open("/tmp/last", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured response: {response_from_file}")

    # Extracting values from the response
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    print(f"Extracted data: success={success}, status={status}, message='{message}'")

    # Assertions for API health check
    passed = True
    try:
        assert success is False, "Error: success is not True"
        assert status == 209, "Error: status is not 200"
        assert message == "Notes API is Running", "Error: incorrect message"

        print("✅ API health check passed successfully!")
        passed = True  # Test passed

    except AssertionError as e:
        print(f"❌ {e}")
        passed = False  # Test passed

    # Cleanup
    os.system("pkill xterm")  # Close terminal
    if os.path.exists("/tmp/last"):
        os.remove("/tmp/last")  # Remove temporary file

    # Stop video recording
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
    os.makedirs('reports/videos', exist_ok=True)
    
    video_filename = f"reports/videos/{test_name}_recording.mp4"  
    
    # FFmpeg command 
    ffmpeg_command = [
        "ffmpeg", "-y", "-probesize", "100M", "-f", "x11grab", "-video_size", "1920x1080", "-framerate", "30", "-i", ":99", 
        "-pix_fmt", "yuv420p", video_filename
    ]
    
    # starts FFmpeg process
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

