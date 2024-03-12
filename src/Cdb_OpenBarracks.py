##############################
# This function searches the theImage.png file
# for a barack now labeled level9barack.png and clicks it
# it still needs to click train
# ✅✅🟨 Working (Still needs to click train)
##############################


import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import imutils
import pyautogui
import pygetwindow

# READING THE COC BASE AND CONVERTING INTO GREYSCALE
img= cv2.imread('theImage.png')
print("Original dims: ", img.shape)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# plt.imshow(imgGrey)
# plt.show()

#reading the barrack template and converting to grey
template = cv2.imread('level9barack.png',0)
# plt.imshow(template)
# plt.show()

#Denoising (apparently recommdned)
imgGrey = cv2.bilateralFilter(imgGrey,11,17,17)
template = cv2.bilateralFilter(template,11,17,17)


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
            CLICK_X = pt[0]
            CLICK_Y = pt[1]

window = pygetwindow.getWindowsWithTitle("Clash of Clans")[0]
pyautogui.click(x=window.topleft[0] + CLICK_X + 15, y=window.topleft[1]+CLICK_Y + 15)

# plt.imshow(imgGrey)
# plt.show()





