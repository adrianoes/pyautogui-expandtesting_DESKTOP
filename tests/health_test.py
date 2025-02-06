import subprocess
import time
import pyautogui
import pyperclip
import json
import os
import re

# Test case function for pytest
def test_curl_response():
    # Run curl directly without opening a graphical terminal
    command = ["curl", "-X", "GET", "https://practice.expandtesting.com/notes/api/health-check", "-H", "accept: application/json"]
    
    # Execute the curl command and get the response
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # If there is an error, print the error message
    if stderr:
        print("Error executing the curl command:", stderr.decode())
    
    # Decode the response to text
    response = stdout.decode()
    
    # Debugging: print the curl response
    print("Curl response is:")
    print(response)
    
    # Regular expression to find a valid JSON in the response text
    json_match = re.search(r'({.*})', response, re.DOTALL)

    if json_match:
        json_response = json_match.group(0)  # Extracts the JSON
    else:
        json_response = "{}"  # If no JSON is found, set an empty JSON

    # Ensure that the 'resources' directory exists
    resources_dir = "resources"
    os.makedirs(resources_dir, exist_ok=True)

    # Save the JSON response to the testdata.json file
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

    # Delete the testdata.json file after the test
    if os.path.exists(json_path):
        os.remove(json_path)
        print(f"File {json_path} has been deleted.")
    
    # Here you can still continue with the graphical automation if needed
    # Close the terminal or any other interaction that needs to be done
    pyautogui.hotkey("alt", "f4")  # Sends Alt+F4 to close the window
