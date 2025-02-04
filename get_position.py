import pyautogui
import time

# Print mouse position every second
print("Move your mouse over the Git Bash window to get its coordinates.")
time.sleep(3)  # Gives you time to prepare

while True:
    x, y = pyautogui.position()
    print(f"Mouse position: x={x}, y={y}")
    time.sleep(1)  # Update every second

