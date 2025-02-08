import time
from faker import Faker
import pyautogui
import os
import json

def test_create_user_curl():
    randomData = Faker().hexify(text='^^^^^^^^^^^^')
    fake = Faker()
    user_email = fake.company_email()
    user_name = fake.name()
    user_password = fake.password()

    # Starting the display
    os.environ["DISPLAY"] = ":99"
    
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

    # User registration
    print("Registering new user...")
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/users/register' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'name={user_name}&email={user_email}&password={user_password}' > /tmp/last"""    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
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
    data = response_json.get("data", {})    
    user_id = data.get("id")
    response_name = data.get("name")
    response_email = data.get("email")

    # Assertions for user registration
    assert success is True, "Error: success is not True"
    assert status == 201, "Error: status is not 201"
    assert message == "User account created successfully", "Error: incorrect message"
    assert response_name == user_name, "Error: name does not match"
    assert response_email == user_email, "Error: email does not match"
    print("✅ User registration test passed successfully!")

    # Save user credentials in a JSON file
    user_data = {
        'user_email': user_email,
        'user_id': user_id,
        'user_name': user_name,
        'user_password': user_password
    }    
    json_file_path = f"./resources/file-{randomData}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    # Print the content of the saved JSON file for double-checking
    print(f"Saved user data in JSON file: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))  # Print the JSON content in a readable format

    # LOGIN PROCESS
    print("Logging in with created user...")

    # Load the user credentials from file
    json_file_path = f"./resources/file-{randomData}.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_email = data['user_email']
        user_password = data['user_password']

    # Send login request
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/users/login' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'email={user_email}&password={user_password}' > /tmp/last"""
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read login response
    with open("/tmp/last", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured login response: {response_from_file}")

    # Extract login response
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    data = response_json.get("data", {})
    user_id_login = data.get("id")
    response_name = data.get("name")
    response_email = data.get("email")
    user_token = data.get("token")

    # Assertions for login
    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Login successful", "Error: incorrect message"
    assert user_id_login == user_id, "Error: user_id does not match"
    assert response_name == user_name, "Error: name does not match"
    assert response_email == user_email, "Error: email does not match"
    print("✅ Login test passed successfully!")

    # Save user credentials in a JSON file
    user_data = {
        'user_email': user_email,
        'user_id': user_id,
        'user_name': user_name,
        'user_password': user_password,
        'user_token': user_token
    }
    json_file_path = f"./resources/file-{randomData}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    # Print the updated JSON content with user token for double-checking
    print(f"Updated user data with token saved in JSON file: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))  # Print the JSON content in a readable format
    print("User token saved successfully!")

    # Deleting the user using the token    
    print("Deleting user...")

    # Load the user token from the saved JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    user_token = data['user_token']

    # Send delete account request
    delete_account_script = f"""curl -X 'DELETE' 'https://practice.expandtesting.com/notes/api/users/delete-account' \
    -H 'accept: application/json' \
    -H 'x-auth-token: {user_token}' > /tmp/last"""
    pyautogui.write(delete_account_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read delete account response
    with open("/tmp/last", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured delete account response: {response_from_file}")

    # Extract delete account response
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    # Assertions for account deletion
    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Account successfully deleted", "Error: incorrect message"
    print("✅ User account deleted successfully!")

    # Close the terminal after testing
    os.system("pkill xterm")
    
    # Delete the JSON file after testing
    os.remove(json_file_path)
    print(f"Deleted JSON file: {json_file_path}")
