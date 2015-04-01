#
#  Crazy Smart Tanks Game 2011

#
#   description:    CST - Main Configuration
#   author:         Vlad Palos
#   date:           13.03.2011
#





from panda3d.core                           import WindowProperties
from pandac.PandaModules                    import ClockObject

RESLIST = [
        "640", "480", 
        "1024", "768", 
        "1280", "960", 
        "1400", "1050"]
        
RES = 2
XRES = int(RESLIST[RES*2])
YRES = int(RESLIST[RES*2+1])
#FULLSCREEN BUG
FULLSCREEN = True
SOUND = True
BRAINS_PATH = "TankBrains/"


def setup():    
    print "Window Default Setup..."    
    wp = WindowProperties() 
    wp.setCursorHidden(False) 
    wp.setSize(int(RESLIST[RES*2]), int(RESLIST[RES*2+1]))
    wp.setFullscreen(FULLSCREEN) 
    base.win.requestProperties(wp) 
#    base.setBackgroundColor(0, 0, 0, 1)

    # Constant FrameRate
    FPS = 30
    globalClock = ClockObject.getGlobalClock()
    globalClock.setMode(ClockObject.MLimited)
    globalClock.setFrameRate(FPS)


def showDebug():
    base.setFrameRateMeter(True)
        
def growRes():
    global XRES, YRES, RES, RESLIST
    print "Increase Resolution"
    if (RES+1)*2 == len(RESLIST):
        RES = 0
    else : 
        RES = RES + 1

    XRES = int(RESLIST[RES*2])
    YRES = int(RESLIST[RES*2+1])
    
    setup()
    

def isFullScreen():
    if (FULLSCREEN) : return "Yes"
    else : return "No"

def switchFullScreen():
    global FULLSCREEN
    
    if (FULLSCREEN) : FULLSCREEN = False
    else : FULLSCREEN = True

    setup()

def isSound():
    if (SOUND) : return "Yes"
    else : return "No"

def switchSound():
    global SOUND

    if (SOUND) : SOUND = False
    else : SOUND = True
    


