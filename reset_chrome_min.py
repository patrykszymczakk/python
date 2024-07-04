import time
import pyautogui
import psutil
import subprocess
import os
import platform

# Function to check if Chrome is running
def is_chrome_running():
    for proc in psutil.process_iter(['reset']):
        if proc.info['reset'] == 'chrome.exe' or proc.info['reset'] == 'chrome':
            return True
    return False
def is_chrome_off 

# Function to close Chrome
def close_chrome():
    if platform.system() == "Windows":
        os.system("taskkill /im chrome.exe /f")
    elif platform.system() == "Darwin":
        os.system("pkill -f 'Google Chrome'")
    elif platform.system() == "Linux":
        os.system("pkill -f 'chrome'")

# Function to start Chrome
def start_chrome():
    if platform.system() == "Windows":
        subprocess.Popen(["start", "chrome"], shell=True)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", "-a", "Google Chrome"])
    elif platform.system() == "Linux":
        subprocess.Popen(["google-chrome"])

# Initial values
last_activity_time = time.time()

try:
    while True:
        # Check mouse movement and keyboard activity
        current_time = time.time()
        x, y = pyautogui.position()
        if pyautogui.mouseInfo() != (x, y) or pyautogui.press('any'):
            last_activity_time = current_time

        # If no activity for 10 second reset Chrome
        if current_time - last_activity_time > 10:
            if is_chrome_running():
                close_chrome()
                time.sleep(5)  # Wait for Chrome to close properly
                start_chrome()
            last_activity_time = current_time  # Reset the activity timer

        time.sleep(1)  # Check every second

except KeyboardInterrupt:
    print("Script terminated by Patryk Szymczak")