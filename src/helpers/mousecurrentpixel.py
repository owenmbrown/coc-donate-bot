### this prints ever 1 second the pixel location of where your mouse is
### ✅✅

import pyautogui
import time

# Ctrl + C in cli to terminate
while(1):
    print(pyautogui.position())
    time.sleep(1)


