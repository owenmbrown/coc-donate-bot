import Cdb_GetImage as gi
import Cdb_OpenBarracks as ob
import Cdb_ClickChat as cc
import Cdb_ClickThis as ct 
import Cdb_TrainTroop as tt
import time
# there has to be a better way to do the above stuff w/o putting all the functions in the same file

# ct.ClickThis("donateBtn.png") ## THIS IS V GLITCHY

# cc.openChat() #✅
# time.sleep(3)
ob.OpenBarracks() #✅
tt.TrainTroop("Barbarian", 5) # not working on big resolution

# gi.getCOCImage()
# ob.openBarracks()
# # cc.openChat()     

