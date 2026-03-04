import pyautogui
import time

#mouse Operation
"""""
pyautogui.click(100,100)
time.sleep(2)
pyautogui.rightClick(100,100)

time.sleep(4)       #waiting time for mouse movement operation

pyautogui.click(1120,974)

pyautogui.doubleClick(100,100)

#pyautogui.drag(100,100, 200,200)

pyautogui.scroll(500)

"""

#Keyboard Operations
"""""
time.sleep(2)

pyautogui.click(911,327)

time.sleep(3)

# pyautogui.write("python rpa_demo_1.py")

# pyautogui.press("enter")

pyautogui.hotkey('ctrl','a')

"""

#image operations

location = pyautogui.locateCenterOnScreen('ai.png', confidence=0.8)

print(location)

time.sleep(2)

pyautogui.click(pyautogui.center(location))

print(pyautogui.size())

hh = pyautogui.screenshot()

hh.save("demo.png")
