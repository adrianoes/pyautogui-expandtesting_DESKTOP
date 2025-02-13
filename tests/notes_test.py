import time
from faker import Faker
import pyautogui
import os
import json
import random

def test_create_note_curl():

    # Generate a random number for custom commands
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Start display
    os.environ["DISPLAY"] = ":99"

    # Start terminal
    starting_terminal()

    # Create user
    create_user(randomData)

    # Log in user
    login_user(randomData)

    print("Creating a new note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user details from JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        user_id = data['user_id']

    # Generate note details
    fake = Faker()
    note_category = fake.random_element(elements=('Home', 'Personal', 'Work'))
    note_description = fake.sentence(3)
    note_title = fake.sentence(2)

    # Send cURL request to create the note
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={note_title}&description={note_description}&category={note_category}' > /tmp/note_response"""
    print(save_output_script)
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from note creation
    with open("/tmp/note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note creation response: {response_from_file}")

    # Extract response data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    data = response_json.get("data", {})

    # Capture note details
    note_id = data.get("id")
    note_created_at = data.get("created_at")
    note_updated_at = data.get("updated_at")
    response_title = data.get("title")
    response_description = data.get("description")
    response_category = data.get("category")
    note_completed = data.get("completed")
    response_user_id = data.get("user_id")

    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Note successfully created", "Error: incorrect message"
    assert note_id is not None, "Error: note_id is None"
    assert response_title == note_title, "Error: title does not match"
    assert response_description == note_description, "Error: description does not match"
    assert response_category == note_category, "Error: category does not match"
    assert note_completed is False, "Error: completed should be False"
    assert response_user_id == user_id, "Error: user_id does not match"
    print("✅ Note creation test passed successfully!")

    # Save user credentials in a JSON file
    os.makedirs('./resources', exist_ok=True)
    user_data = {
        'user_id': user_id,
        'user_token': user_token,
        'note_category': note_category,
        'note_completed': note_completed,
        'note_description': note_description,
        'note_title': note_title,
        'note_id': note_id,
        'note_created_at': note_created_at,
        'note_updated_at': note_updated_at
    }
    json_file_path = f"./resources/file-{randomData}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    # Print the content of the saved JSON file for double-checking
    print(f"Saved user data in JSON file: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))  # Print the JSON content in a readable format

    # Delete user after the test
    delete_user(randomData)

    # Close terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_create_note_bad_request_curl():

    # Generate a random number for custom commands
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Start display
    os.environ["DISPLAY"] = ":99"

    # Start terminal
    starting_terminal()

    # Create user
    create_user(randomData)

    # Log in user
    login_user(randomData)

    print("Creating a new note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user details from JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']

    # Generate note details
    fake = Faker()
    note_description = fake.sentence(3)
    note_title = fake.sentence(2)

    # Send cURL request to create the note
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={note_title}&description={note_description}&category=a' > /tmp/note_response"""
    print(save_output_script)
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from note creation
    with open("/tmp/note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note creation response: {response_from_file}")

    # Extract response data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 400, "Error: status is not 400"
    assert message == "Category must be one of the categories: Home, Work, Personal", "Error: incorrect message"

    # Delete user after the test
    delete_user(randomData)

    # Close terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_create_note_unauthorized_curl():

    # Generate a random number for custom commands
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Start display
    os.environ["DISPLAY"] = ":99"

    # Start terminal
    starting_terminal()

    # Create user
    create_user(randomData)

    # Log in user
    login_user(randomData)

    print("Creating a new note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user details from JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']

    # Generate note details
    fake = Faker()
    note_category = fake.random_element(elements=('Home', 'Personal', 'Work'))
    note_description = fake.sentence(3)
    note_title = fake.sentence(2)

    # Send cURL request to create the note
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: @{user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={note_title}&description={note_description}&category={note_category}' > /tmp/note_response"""
    print(save_output_script)
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from note creation
    with open("/tmp/note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note creation response: {response_from_file}")

    # Extract response data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 401, "Error: status is not 401"
    assert message == "Access token is not valid or has expired, you will need to login", "Error: incorrect message"

    # Delete user after the test
    delete_user(randomData)

    # Close terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_get_notes_curl():

    # Generate a random number for custom commands
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Start display
    os.environ["DISPLAY"] = ":99"

    # Start terminal
    starting_terminal()

    # Create user
    create_user(randomData)

    # Log in user
    login_user(randomData)

    create_note(randomData)

    print("Creating a new note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user details from JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        user_id = data['user_id']
        note_category = data['note_category']
        note_completed = data['note_completed']
        note_description = data['note_description']
        note_title = data['note_title']
        note_id = data['note_id']
        note_created_at = data['note_created_at']
        note_updated_at = data['note_updated_at']

    # Generate note details
    fake = Faker()
    note_category2 = fake.random_element(elements=('Home', 'Personal', 'Work'))
    note_description2 = fake.sentence(3)
    note_title2 = fake.sentence(2)

    # Send cURL request to create the note
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={note_title2}&description={note_description2}&category={note_category2}' > /tmp/note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from note creation
    with open("/tmp/note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note creation response: {response_from_file}")

    # Extract response data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    data = response_json.get("data", {})

    # Capture note details
    note_id2 = data.get("id")
    note_created_at2 = data.get("created_at")
    note_updated_at2 = data.get("updated_at")
    note_title2 = data.get("title")
    note_description2 = data.get("description")
    note_category2 = data.get("category")
    note_completed2 = data.get("completed")

    # Send cURL request to retrieve all notes
    save_output_script = f"""curl -X 'GET' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: {user_token}' > /tmp/notes_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the file
    with open("/tmp/notes_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured response: {response_from_file}")

    # Extract values from the response
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    data = response_json.get("data", [])

    # Validate if at least two notes exist
    assert len(data) >= 2, "Error: Less than 2 notes retrieved"

    # First created note (data[1])
    response_note_id = data[1].get("id")
    response_note_created_at = data[1].get("created_at")
    response_note_updated_at = data[1].get("updated_at")
    response_note_title = data[1].get("title")
    response_note_description = data[1].get("description")
    response_note_category = data[1].get("category")
    response_note_completed = data[1].get("completed")
    response_user_id = data[1].get("user_id")

    # Second created note (data[0])
    response_note_id2 = data[0].get("id")
    response_note_created_at2 = data[0].get("created_at")
    response_note_updated_at2 = data[0].get("updated_at")
    response_note_title2 = data[0].get("title")
    response_note_description2 = data[0].get("description")
    response_note_category2 = data[0].get("category")
    response_note_completed2 = data[0].get("completed")
    response_user_id2 = data[0].get("user_id")

    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Notes successfully retrieved", "Error: incorrect message"

    # Assertions for first created note (data[1])
    assert response_note_id == note_id, "Error: note_id does not match"
    assert response_note_title == note_title, "Error: title does not match"
    assert response_note_description == note_description, "Error: description does not match"
    assert response_note_category == note_category, "Error: category does not match"
    assert response_note_completed == note_completed, "Error: completed does not match"
    assert response_note_created_at == note_created_at, "Error: note_created_at does not match"
    assert response_note_updated_at == note_updated_at, "Error: note_updated_at does not match"
    assert response_user_id == user_id, "Error: user_id does not match"

    # Assertions for second created note (data[0])
    assert response_note_id2 == note_id2, "Error: note_id2 does not match"
    assert response_note_title2 == note_title2, "Error: title2 does not match"
    assert response_note_description2 == note_description2, "Error: description2 does not match"
    assert response_note_category2 == note_category2, "Error: category2 does not match"
    assert response_note_completed2 == note_completed2, "Error: completed2 does not match"
    assert response_note_created_at2 == note_created_at2, "Error: note_created_at2 does not match"
    assert response_note_updated_at2 == note_updated_at2, "Error: note_updated_at2 does not match"
    assert response_user_id2 == user_id, "Error: user_id2 does not match"
    print("✅ Notes retrieval test passed successfully!")

    # Delete user after the test
    delete_user(randomData)

    # Close terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_get_notes_unauthorized_curl():

    # Generate a random number for custom commands
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Start display
    os.environ["DISPLAY"] = ":99"

    # Start terminal
    starting_terminal()

    # Create user
    create_user(randomData)

    # Log in user
    login_user(randomData)

    create_note(randomData)

    print("Creating a new note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user details from JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']

    # Generate note details
    fake = Faker()
    note_category2 = fake.random_element(elements=('Home', 'Personal', 'Work'))
    note_description2 = fake.sentence(3)
    note_title2 = fake.sentence(2)

    # Send cURL request to create the note
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={note_title2}&description={note_description2}&category={note_category2}' > /tmp/note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from note creation
    with open("/tmp/note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note creation response: {response_from_file}")

    # Extract response data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    data = response_json.get("data", {})

    # Send cURL request to retrieve all notes
    save_output_script = f"""curl -X 'GET' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: @{user_token}' > /tmp/notes_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the file
    with open("/tmp/notes_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured response: {response_from_file}")

    # Extract values from the response
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 401, "Error: status is not 401"
    assert message == "Access token is not valid or has expired, you will need to login", "Error: incorrect message"

    # Delete user after the test
    delete_user(randomData)

    # Close terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_get_note_by_id_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Retrieving note by ID...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        user_id = data['user_id']
        note_id = data['note_id']  # Retrieve the created note ID

    # cURL command to fetch the note by its ID
    save_output_script = f"""curl -X 'GET' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: {user_token}' > /tmp/get_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/get_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note retrieval response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    note_data = response_json.get("data", {})

    # Capture returned note details
    response_note_id = note_data.get("id")
    response_title = note_data.get("title")
    response_description = note_data.get("description")
    response_category = note_data.get("category")
    note_completed = note_data.get("completed")
    note_created_at = note_data.get("created_at")
    note_updated_at = note_data.get("updated_at")
    response_user_id = note_data.get("user_id")

    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Note successfully retrieved", "Error: incorrect message"
    assert response_note_id == note_id, "Error: note_id does not match"
    assert response_title == data['note_title'], "Error: title does not match"
    assert response_description == data['note_description'], "Error: description does not match"
    assert response_category == data['note_category'], "Error: category does not match"
    assert note_completed == data['note_completed'], "Error: completed status does not match"
    assert response_user_id == user_id, "Error: user_id does not match"
    assert note_created_at == data['note_created_at'], "Error: created_at does not match"
    assert note_updated_at == data['note_updated_at'], "Error: updated_at does not match"
    print("✅ Note retrieval test passed successfully!")

    # Display the saved JSON content for verification
    print(f"JSON file after note retrieval test: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_get_note_by_id_unauthorized_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Retrieving note by ID...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # cURL command to fetch the note by its ID
    save_output_script = f"""curl -X 'GET' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: @{user_token}' > /tmp/get_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/get_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note retrieval response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 401, "Error: status is not 401"
    assert message == "Access token is not valid or has expired, you will need to login", "Error: incorrect message"

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_update_note_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Updating the note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        user_id = data['user_id']
        note_id = data['note_id']  # Retrieve the created note ID
        note_created_at = data['note_created_at']   # Retrieve updated_at for comparison
        note_updated_at = data['note_updated_at']

    # Generate new values for the note
    fake = Faker()
    updated_note_category = fake.random_element(elements=('Home', 'Personal', 'Work'))
    updated_note_description = fake.sentence(3)
    updated_note_title = fake.sentence(2)

    # cURL command to update the note by its ID
    save_output_script = f"""curl -X 'PUT' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={updated_note_title}&description={updated_note_description}&completed=true&category={updated_note_category}' > /tmp/update_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/update_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note update response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    response_note_data = response_json.get("data", {})

    # Capture returned updated note details
    response_note_id = response_note_data.get("id")
    response_title = response_note_data.get("title")
    response_description = response_note_data.get("description")
    response_category = response_note_data.get("category")
    response_completed = response_note_data.get("completed")
    response_created_at = response_note_data.get("created_at")
    response_updated_at = response_note_data.get("updated_at")
    response_user_id = response_note_data.get("user_id")

    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Note successfully Updated", "Error: incorrect message"
    assert response_note_id == note_id, "Error: note_id does not match"
    assert response_title == updated_note_title, "Error: title does not match"
    assert response_description == updated_note_description, "Error: description does not match"
    assert response_category == updated_note_category, "Error: category does not match"
    assert response_completed is True, "Error: completed status does not match"
    assert response_user_id == user_id, "Error: user_id does not match"
    assert response_created_at == note_created_at, "Error: created_at should not be updated"
    assert response_updated_at != note_updated_at, "Error: updated_at should be different from the previous one"
    print("✅ Note update test passed successfully!")

    # Display the saved JSON content for verification
    print(f"JSON file after note update test: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_update_note_bad_request_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Updating the note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # Generate new values for the note
    fake = Faker()
    updated_note_description = fake.sentence(3)
    updated_note_title = fake.sentence(2)

    # cURL command to update the note by its ID
    save_output_script = f"""curl -X 'PUT' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={updated_note_title}&description={updated_note_description}&completed=true&category=a' > /tmp/update_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/update_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note update response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 400, "Error: status is not 400"
    assert message == "Category must be one of the categories: Home, Work, Personal", "Error: incorrect message"

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_update_note_unauthorized_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Updating the note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # Generate new values for the note
    fake = Faker()
    updated_note_category = fake.random_element(elements=('Home', 'Personal', 'Work'))
    updated_note_description = fake.sentence(3)
    updated_note_title = fake.sentence(2)

    # cURL command to update the note by its ID
    save_output_script = f"""curl -X 'PUT' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: @{user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={updated_note_title}&description={updated_note_description}&completed=true&category={updated_note_category}' > /tmp/update_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/update_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note update response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 401, "Error: status is not 401"
    assert message == "Access token is not valid or has expired, you will need to login", "Error: incorrect message"

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_update_note_status_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Patching the note to update its completion status...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        user_id = data['user_id']
        note_id = data['note_id']  # Retrieve the created note ID
        note_category = data['note_category']
        note_description = data['note_description']
        note_title = data['note_title']
        note_created_at = data['note_created_at']  # Retrieve created_at for comparison
        note_updated_at = data['note_updated_at']  # Retrieve updated_at for comparison

    # cURL command to update the note's completion status
    save_output_script = f"""curl -X 'PATCH' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'completed=true' > /tmp/patch_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/patch_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note patch response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    response_note_data = response_json.get("data", {})

    # Capture returned updated note details
    response_note_id = response_note_data.get("id")
    response_title = response_note_data.get("title")
    response_description = response_note_data.get("description")
    response_category = response_note_data.get("category")
    response_completed = response_note_data.get("completed")
    response_created_at = response_note_data.get("created_at")
    response_updated_at = response_note_data.get("updated_at")
    response_user_id = response_note_data.get("user_id")

    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Note successfully Updated", "Error: incorrect message"
    assert response_note_id == note_id, "Error: note_id does not match"
    assert response_title == note_title, "Error: title does not match"
    assert response_description == note_description, "Error: description does not match"
    assert response_category == note_category, "Error: category does not match"
    assert response_completed is True, "Error: completed status was not updated correctly"
    assert response_user_id == user_id, "Error: user_id does not match"
    assert response_created_at == note_created_at, "Error: created_at should not be updated"
    assert response_updated_at != note_updated_at, "Error: updated_at should be different from the previous one (due to PATCH)"
    print("✅ Note patch test passed successfully!")

    # Display the saved JSON content for verification
    print(f"JSON file after note patch test: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_update_note_status_bad_request_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Patching the note to update its completion status...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # cURL command to update the note's completion status
    save_output_script = f"""curl -X 'PATCH' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'completed=a' > /tmp/patch_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/patch_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note patch response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 400, "Error: status is not 400"
    assert message == "Note completed status must be boolean", "Error: incorrect message"

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_update_note_status_unauthorized_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Patching the note to update its completion status...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # cURL command to update the note's completion status
    save_output_script = f"""curl -X 'PATCH' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: @{user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'completed=true' > /tmp/patch_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/patch_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note patch response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 401, "Error: status is not 401"
    assert message == "Access token is not valid or has expired, you will need to login", "Error: incorrect message"

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_delete_note_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Deleting the note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # cURL command to delete the note by its ID
    save_output_script = f"""curl -X 'DELETE' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: {user_token}' > /tmp/delete_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/delete_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note deletion response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Note successfully deleted", "Error: incorrect message"
    print("✅ Note deletion test passed successfully!")

    # Display the saved JSON content for verification
    print(f"JSON file after note deletion test: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_delete_note_bad_request_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Deleting the note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # cURL command to delete the note by its ID
    save_output_script = f"""curl -X 'DELETE' 'https://practice.expandtesting.com/notes/api/notes/@{note_id}' -H 'accept: application/json' -H 'x-auth-token: {user_token}' > /tmp/delete_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/delete_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note deletion response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 400, "Error: status is not 400"
    assert message == "Note ID must be a valid ID", "Error: incorrect message"

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def test_delete_note_unauthorized_curl():

    # Generate a random identifier
    randomData = Faker().hexify(text='^^^^^^^^^^^^')

    # Set display
    os.environ["DISPLAY"] = ":99"

    # Start the terminal
    starting_terminal()

    # Create a user
    create_user(randomData)

    # Log in the user
    login_user(randomData)

    # Create a note and save its details in the JSON file
    create_note(randomData)

    print("Deleting the note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user and note details from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        note_id = data['note_id']  # Retrieve the created note ID

    # cURL command to delete the note by its ID
    save_output_script = f"""curl -X 'DELETE' 'https://practice.expandtesting.com/notes/api/notes/{note_id}' -H 'accept: application/json' -H 'x-auth-token: @{user_token}' > /tmp/delete_note_response"""
    
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from the cURL command
    with open("/tmp/delete_note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note deletion response: {response_from_file}")

    # Extract response JSON data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")

    assert success is False, "Error: success is not False"
    assert status == 401, "Error: status is not 401"
    assert message == "Access token is not valid or has expired, you will need to login", "Error: incorrect message"

    # Delete the user after the test
    delete_user(randomData)

    # Close the terminal
    os.system("pkill xterm")

    # Delete the created JSON file
    delete_json_file(randomData)

def create_user(randomData):
    # User registration
    print("Registering new user...")
    fake = Faker()
    user_email = fake.company_email()
    user_name = fake.name()
    password_length = random.randint(8, 28) # The &character is not supported. In case random function choose a special character, it will choose inside the range below, which does not contains &.
    while True:
        user_password = fake.password(length=password_length)
        if "&" not in user_password:
            break 
    print(user_password)   
    
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/users/register' -H 'accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -d 'name={user_name}&email={user_email}&password={user_password}' > /tmp/last"""    

    print(user_password)
    print(save_output_script)
    pyautogui.write(save_output_script, interval=0.1)
    time.sleep(2)     
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
    os.makedirs('./resources', exist_ok=True)
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

def login_user(randomData):
    print("Logging in with created user...")

    # Load the user credentials from file
    json_file_path = f"./resources/file-{randomData}.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_email = data['user_email']
        user_password = data['user_password']
        user_name = data['user_name']
        user_id = data['user_id']

    # Send login request
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/users/login' -H 'accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -d 'email={user_email}&password={user_password}' > /tmp/last"""
    
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
    response_user_id = data.get("id")
    response_name = data.get("name")
    response_email = data.get("email")
    user_token = data.get("token")

    # Assertions for login
    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Login successful", "Error: incorrect message"
    assert response_user_id == user_id, "Error: user_id does not match"
    assert response_name == user_name, "Error: name does not match"
    assert response_email == user_email, "Error: email does not match"
    print("✅ Login test passed successfully!")

    # Save user credentials in a JSON file
    os.makedirs('./resources', exist_ok=True)
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

def delete_user(randomData):    
    print("Deleting user...")

    # Load the user credentials from file
    json_file_path = f"./resources/file-{randomData}.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    user_token = data['user_token']

    # Send delete account request
    save_output_script = f"""curl -X 'DELETE' 'https://practice.expandtesting.com/notes/api/users/delete-account' -H 'accept: application/json' -H 'x-auth-token: {user_token}' > /tmp/last"""
    
    pyautogui.write(save_output_script, interval=0.1)
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

def delete_json_file(randomData):
    # Delete the JSON file after testing
    json_file_path = f"./resources/file-{randomData}.json"
    os.remove(json_file_path)
    print(f"Deleted JSON file: {json_file_path}")

def create_note(randomData):
    print("Creating a new note...")

    # JSON file path (must remain the same to avoid deletion issues)
    json_file_path = f"./resources/file-{randomData}.json"

    # Load user details from JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        user_token = data['user_token']
        user_id = data['user_id']

    # Generate note details
    fake = Faker()
    note_category = fake.random_element(elements=('Home', 'Personal', 'Work'))
    note_description = fake.sentence(3)
    note_title = fake.sentence(2)

    # Send cURL request to create the note
    save_output_script = f"""curl -X 'POST' 'https://practice.expandtesting.com/notes/api/notes' -H 'accept: application/json' -H 'x-auth-token: {user_token}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'title={note_title}&description={note_description}&category={note_category}' > /tmp/note_response"""
    print(save_output_script)
    pyautogui.write(save_output_script, interval=0.1)
    pyautogui.press("enter")
    time.sleep(10)

    # Read the response from note creation
    with open("/tmp/note_response", "r") as file:
        response_from_file = file.read().strip()
    print(f"Captured note creation response: {response_from_file}")

    # Extract response data
    response_json = json.loads(response_from_file)
    success = response_json.get("success")
    status = response_json.get("status")
    message = response_json.get("message")
    data = response_json.get("data", {})

    # Capture note details
    note_id = data.get("id")
    note_created_at = data.get("created_at")
    note_updated_at = data.get("updated_at")
    response_title = data.get("title")
    response_description = data.get("description")
    response_category = data.get("category")
    note_completed = data.get("completed")
    response_user_id = data.get("user_id")

    assert success is True, "Error: success is not True"
    assert status == 200, "Error: status is not 200"
    assert message == "Note successfully created", "Error: incorrect message"
    assert note_id is not None, "Error: note_id is None"
    assert response_title == note_title, "Error: title does not match"
    assert response_description == note_description, "Error: description does not match"
    assert response_category == note_category, "Error: category does not match"
    assert note_completed is False, "Error: completed should be False"
    assert response_user_id == user_id, "Error: user_id does not match"
    print("✅ Note creation test passed successfully!")

    # Save user credentials in a JSON file
    os.makedirs('./resources', exist_ok=True)
    user_data = {
        'user_id': user_id,
        'user_token': user_token,
        'note_category': note_category,
        'note_completed': note_completed,
        'note_description': note_description,
        'note_title': note_title,
        'note_id': note_id,
        'note_created_at': note_created_at,
        'note_updated_at': note_updated_at
    }
    json_file_path = f"./resources/file-{randomData}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    # Print the content of the saved JSON file for double-checking
    print(f"Saved user data in JSON file: {json_file_path}")
    with open(json_file_path, 'r') as json_file:
        print(json.dumps(json.load(json_file), indent=4))  # Print the JSON content in a readable format