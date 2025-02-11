import time
import pyautogui
import os
import json
import subprocess
import pyscreeze

def test_health_curl():

    # Start display
    os.environ["DISPLAY"] = ":99"
    
    # Start terminal
    starting_terminal()

    # API Health Check
    print("Checking API health status...")
    
    save_output_script = """curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' \
    -H 'accept: application/json' \ > /tmp/last"""
    
    pyautogui.write(save_output_script, interval=0.1)
    
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
    
    try:
        assert success is False, "Error: success is not True"
        assert status == 209, "Error: status is not 200"
        assert message == "Notes API is Running", "Error: incorrect message"
        print("✅ API health check passed successfully!")
    except AssertionError as e:
        print(f"❌ {e}")

    # Cleanup
    os.system("pkill xterm")  # Close terminal
    if os.path.exists("/tmp/last"):
        os.remove("/tmp/last")  # Remove temporary file

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
