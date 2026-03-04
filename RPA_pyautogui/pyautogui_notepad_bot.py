import pyautogui
import time
from datetime import datetime
import os

print("Starting Notepad Automation Bot...")

# Small delay so you can see bot start
time.sleep(2)

# Step 1: Open Notepad
os.system("start notepad")
time.sleep(2)

# Step 2: Prepare report content
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = f"""
DAILY AUTOMATION REPORT
-----------------------
Date & Time: {today}

Tasks Completed:
- Checked emails
- Updated project status
- Submitted report

Status: SUCCESS
"""

# Step 3: Type the report
pyautogui.write(report, interval=0.03)

time.sleep(1)

# Step 4: Save the file
pyautogui.hotkey("ctrl", "s")
time.sleep(2)

# Type file name
filename = f"Daily_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
pyautogui.write(filename)
time.sleep(1)

pyautogui.press("enter")

# Step 5: Confirmation popup
pyautogui.alert("✅ Report created and saved successfully!", title="Automation Complete")

print("Automation Finished!")