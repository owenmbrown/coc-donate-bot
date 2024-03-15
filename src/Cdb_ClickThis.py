######################
# Takes photo of the CoC and searches it for
# argument 'forThis' which is assumed to be a string
# this can replace Cdb_OpenBarracks.py btw if we want
# ✅✅✅ Working, a little slow tho
######################

#it should return -1 if it failed to find the image this is NOT TESTED THO

import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import imutils
import pyautogui
import pygetwindow
import Cdb_GetImage as gi
import time

def ClickThis(forThis):
    gi.getCOCImage()
    img= cv2.imread("images\\theImage.png")
    # print("Original dims: ", img.shape)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # plt.imshow(imgGrey)
    # plt.show()

    #reading the barrack template and converting to grey
    temp2 = "images\\" + forThis
    template = cv2.imread(temp2,0) 
    # plt.imshow(template)
    # plt.show()

    #Denoising (apparently recommdned)
    imgGrey = cv2.bilateralFilter(imgGrey,11,17,17)
    template = cv2.bilateralFilter(template,11,17,17)

    click_xx = -1
    #scaling for every plausible scale
    for scale in np.linspace(0.2,1.0,20)[::-1]:
        resized = imutils.resize(template,width=int(template.shape[1]*scale))
        rotTemp = imutils.rotate(resized, 0) #no rotation, ig its unneeded
        w, h = rotTemp.shape[::-1]

        res = cv2.matchTemplate(imgGrey, rotTemp, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8 # all docs said use 0.8 for basic things like this
        loc = np.where( res >= threshold)

        if loc:
            for pt in zip(*loc[::-1]):
                cv2.rectangle(imgGrey, pt, (pt[0] + w, pt[1]+h), (0,0,255), 2)
                # print(pt[0], ",", pt[1])
                click_xx = pt[0]
                click_yy = pt[1]

    if click_xx != -1:
        print("found *forThis*")
        window = pygetwindow.getWindowsWithTitle("Clash of Clans")[0]
        pyautogui.click(x=window.topleft[0] + click_xx + 15, y=window.topleft[1]+click_yy + 15)
    else:
        print("did NOT find *forThis*")
        return -1