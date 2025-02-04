import pyautogui
import subprocess
import time
import pyperclip

# 1️⃣ Open the Command Prompt (CMD)
subprocess.Popen("cmd.exe", shell=True)
time.sleep(20)  # Wait for the CMD window to open

# 2️⃣ Click on the CMD window (adjust the coordinates if needed)
pyautogui.click(x=1210, y=1050)

# 3️⃣ Type a curl command and press Enter
command = "curl -X GET https://jsonplaceholder.typicode.com/posts/1"
pyautogui.write(command)
pyautogui.press("enter")

# 4️⃣ Wait for the command response
time.sleep(20)

# 5️⃣ Select and copy the terminal output
pyautogui.hotkey("ctrl", "a")  # Select all text
pyautogui.hotkey("ctrl", "c")  # Copy text

# 6️⃣ Retrieve the copied text and display it in the VS Code terminal
copied_text = pyperclip.paste()
print("\n📝 Copied Content from CMD:\n", copied_text)
