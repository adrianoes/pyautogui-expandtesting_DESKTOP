import pyautogui
import subprocess
import time
import pyperclip
import json
import os

# Test case function for pytest
def test_curl_response():
    # Open the Command Prompt (CMD)
    subprocess.Popen("cmd.exe", shell=True)
    time.sleep(5)  # Wait for the CMD window to open

    # Click on the CMD window (adjust the coordinates as necessary)
    pyautogui.click(x=1180, y=1050)
    time.sleep(5)
    pyautogui.hotkey("win", "up")  # Maximize the terminal window
    time.sleep(2)
    pyautogui.click(x=800, y=450)
    time.sleep(2)

    # Type the curl command and press Enter
    command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    pyperclip.copy(command)  # Copy the command to the clipboard
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")  # Paste the command
    pyautogui.press("enter")  # Execute the command

    # Wait for the command response
    time.sleep(5)

    # Select and copy the response from Git Bash
    pyautogui.hotkey("ctrl", "shift", "a")  # Select all text
    time.sleep(2)  # Ensure the selection is complete
    pyautogui.hotkey("ctrl", "c")  # Copy the selection
    time.sleep(2)  # Ensure the copy is complete

    # Retrieve the copied text
    copied_text = pyperclip.paste()

    # Extract the JSON response from the copied text
    start = copied_text.find("{")  # Find the start of the JSON
    end = copied_text.rfind("}")  # Find the end of the JSON
    if start != -1 and end != -1:
        json_response = copied_text[start : end + 1]  # Extract JSON
    else:
        json_response = "{}"  # Default empty JSON if not found

    # Ensure the 'resources' directory exists
    resources_dir = "resources"
    os.makedirs(resources_dir, exist_ok=True)

    # Save the JSON response to a file
    json_path = os.path.join(resources_dir, "testdata.json")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(json.loads(json_response), json_file, indent=4)

    # Read the JSON file and extract variables
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    success = data.get("success")
    status = data.get("status")
    message = data.get("message")

    # Perform assertions to validate the response
    assert success == True, f"Expected success=True but got {success}"
    assert status == 200, f"Expected status=200 but got {status}"
    assert message == "Notes API is Running", f"Expected message='Notes API is Running' but got {message}"

    os.remove(json_path)  # Delete testdata.json