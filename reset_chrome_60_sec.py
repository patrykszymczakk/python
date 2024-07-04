import time
import pyautogui
import psutil
import subprocess
import os

# Function to check if Chrome is running
def is_chrome_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'chrome.exe':
            return True
    return False

# Function to close Chrome
def close_chrome():
    os.system("taskkill /im chrome.exe /f")

# Function to start Chrome
def start_chrome():
    subprocess.Popen(["start", "chrome"], shell=True)

# Initial values
last_activity_time = time.time()
last_mouse_position = pyautogui.position()

try:
    while True:
        # Check mouse movement
        current_mouse_position = pyautogui.position()
        if current_mouse_position != last_mouse_position:
            last_activity_time = time.time()
            last_mouse_position = current_mouse_position

        # Check keyboard activity by looking for any key press
        if pyautogui.press('esc'):  # Using 'esc' as a placeholder for any key press
            last_activity_time = time.time()

        # If no activity for 1 minute, reset Chrome
        if time.time() - last_activity_time > 60:
            if is_chrome_running():
                close_chrome()
                time.sleep(5)  # Wait for Chrome to close properly
                start_chrome()
            last_activity_time = time.time()  # Reset the activity timer

        time.sleep(1)  # Check every second

except KeyboardInterrupt:
    print("Script terminated by user.")