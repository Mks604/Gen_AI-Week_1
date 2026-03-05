RPA Automation using PyAutoGUI
📌 Overview

This project demonstrates Robotic Process Automation (RPA) using Python and the PyAutoGUI library.
PyAutoGUI allows Python scripts to control the mouse and keyboard to automate repetitive tasks on a computer interface.

The goal of this project is to automate simple GUI-based operations such as:

Mouse movements

Mouse clicks

Keyboard typing

Opening applications

Automating repetitive desktop tasks

🚀 Features

Automates mouse movements and clicks

Automates keyboard inputs

Executes repetitive tasks automatically

Simulates human interaction with the GUI

Simple Python scripts for desktop automation

🛠️ Technologies Used

Python 3

PyAutoGUI

PyAutoGUI is a cross-platform Python library that enables scripts to control mouse and keyboard actions programmatically.

📂 Project Structure
RPA_pyautogui/
│
├── automation_script.py
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Mks604/Gen_AI-Week_1.git
2️⃣ Navigate to the Project Folder
cd Gen_AI-Week_1/RPA_pyautogui
3️⃣ Install Required Packages
pip install pyautogui
▶️ Usage

Run the Python script to start the automation.

python automation_script.py

Example automation script:

import pyautogui
import time

time.sleep(5)

pyautogui.moveTo(500, 300)
pyautogui.click()

pyautogui.write("Hello, this is automated typing!", interval=0.1)

pyautogui.press("enter")
📸 Example Use Cases

Automatically filling forms

Desktop task automation

Automated testing of GUI applications

Repetitive data entry tasks

⚠️ Notes

Ensure the screen resolution matches the coordinates used in the script.

Do not move the mouse during automation unless required.

Add delays (time.sleep()) to avoid execution errors.



📜 License

This project is open-source and available under the MIT License.
