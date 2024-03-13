##############################
# This function finds and clicks the chat button
# from theImage.png
# ✅✅✅ working
##############################

from PIL import Image
import pyautogui
import pygetwindow

def openChat():
    windowTitle = "Clash of Clans"
    window = pygetwindow.getWindowsWithTitle(windowTitle)[0]
    middleAxis = (window.topleft[1] + window.bottomright[1] - 28)//2 #gets the horizontal middle axis in pixels and -28 b/c of title bar windows says it is 32 but i measured and it is ~28
    

    # print("MIDDLEAXIS: ", middleAxis) # THIS WORK plus/minus 4 pixels
    # ~45 pixels will work on both full screen and tiny we need to test this tho also its a little off on fullscreen but still clicks the button

    pyautogui.click(x=window.topleft[0] + 45, y=middleAxis)