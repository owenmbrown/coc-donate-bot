##############################
# Takes input of string of troop, ie for
# dragon: "Dragon" use '_' for spaces ie.
# "Baby_Dragon" and 'S' prefix for super troops
# ie "S_Archer" and also the number
# of troops you want to train (default is 1)
# ✅✅✅ Working

# Note I chose not to just call Cdb_ClickThis b/c it 
# would have to search the image quantity times which was pretty slow
# i think we should still add randomness to this too in the clicks
##############################
import Cdb_Globals as const
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import imutils
import pyautogui
import pygetwindow
import Cdb_GetImage as gi
import time
import Cdb_ClickThis as ct

def TrainTroop(troop, quantity = 1):
    if troop is None:
        print("Passed in troop is empty")
        return -1

    gi.getCOCImage()
    img= cv2.imread("images\\theImage.png")
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # plt.ims

    temp2 = "images\\" + const.TROOPS[troop]
    template = cv2.imread(temp2,0) 

    imgGrey = cv2.bilateralFilter(imgGrey,11,17,17)
    template = cv2.bilateralFilter(template,11,17,17)


    for scale in np.linspace(0.2,1.0,20)[::-1]:
        resized = imutils.resize(template,width=int(template.shape[1]*scale))
        rotTemp = imutils.rotate(resized, 0)
        w, h = rotTemp.shape[::-1]

        res = cv2.matchTemplate(imgGrey, rotTemp, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)

        if loc:
            for pt in zip(*loc[::-1]):
                cv2.rectangle(imgGrey, pt, (pt[0] + w, pt[1]+h), (0,0,255), 2)
                click_x1 = pt[0]
                click_y1 = pt[1]

    window = pygetwindow.getWindowsWithTitle("Clash of Clans")[0]

    for i in range(quantity):
        pyautogui.click(x=window.topleft[0] + click_x1 + 15, y=window.topleft[1] + click_y1 + 15)
    
    # updating the army comp
    # 🐒🐒 but what if it is already full we need to make sure there are no bugs in donating and training on decrementing and incrementing const.currentArmy
    const.currentArmy[troop] = const.currentArmy[troop] + quantity 


