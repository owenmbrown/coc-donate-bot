#######################
# This is a hard function
# maybe scrap all of the below logic i was trying to throw something togeter super quick
# 🟥🟥🟥 
#######################

import Cdb_ClickThis as ct
import Cdb_ClickChat as cc
import Cdb_Globals as const
import time

def P_greenUp():
    if ct.ClickThis("Green_Up.png")==-1:
        return -1

#this may b unneccssary if it just goes up to the next one from the starting locaiton in the chat
def P_greenDown():
    if ct.ClickThis("Green_Down.png")==-1:
        return -1

#update globals in this (const)
def P_donateAction():
    ct.ClickThis("donateBtn.png")
    time.sleep(15)
    print("\nafter it was calledn\n")
    # ADD LOGIC:
        
        #(1) Click each troop that is not greyed out and decrement the respective 

def donate():
    cc.openChat()
    time.sleep(1)
    while (P_donateAction() != -1):
        continue
    # while (P_greenUP() != -1):
    #     P_donateAction()
    # while (P_greenDown() != -1):
    #     P_donateAction()
    