##############################
# This function takes a screenshot of the
# COC page and saves it to theImage.png.
# This needs COC on top of everything and immediatley viewable
# ✅✅✅ Working
##############################

from PIL import Image
import pyautogui
import pygetwindow
import os

# titles = pygetwindow.getAllTitles() #gets all window titles *just for testing COC=> "Clash of Clans"

#ADD TRY AND EXCEPT TO SEE IF COC is open or not and continue running this to hold up the other programs dependent on getimage
def getCOCImage(windowTitle = "Clash of Clans"):
    window = pygetwindow.getWindowsWithTitle(windowTitle)[0]

    SAVE_PATH = os.path.join(os.path.dirname(__file__), "theImage.png") #change this to whereever we want to save the images maybe in a special folder
    print(SAVE_PATH)

    pyautogui.screenshot(SAVE_PATH)
    im = Image.open(SAVE_PATH)


    lhs = window.topleft[0]
    top = window.topleft[1]
    rhs = window.bottomright[0]
    bot = window.bottomright[1]

    im = im.crop((lhs,top,rhs,bot))
    im.save(SAVE_PATH)
    # im.show(SAVE_PATH) # opens up image in default image viewer


getCOCImage() #uncomment to test for now until tests are working