import time
import pyautogui
import os
import json

def test_health_curl():

    #starting the display
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

    # Command cURL - If it is a get request, it ca be requested twice so you can observe the proper answer in the terminal screen.
    # curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    # pyautogui.write(curl_command, interval=0.15)
    # pyautogui.press("enter")
    # print("cURL command executed.")

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
            print("✅ Test passed successfully!")
        except json.JSONDecodeError:
            print("❌ Error converting the response to JSON!")
    else:
        print("❌ Response was not captured correctly.")

    # Close the terminal after capturing the response
    os.system("pkill xterm")

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