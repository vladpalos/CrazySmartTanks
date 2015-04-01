#
#  Crazy Smart Tanks Game 2011

#
#
#
#
#

import cst_FtConfig
from direct.showbase.DirectObject               import DirectObject

import os
import sys
from math                                       import pi, sin, cos

from direct.task                                import Task    
from direct.gui.DirectGui                       import *

from cst_GuiBox                                 import cst_GuiBox
from cst_Game                                   import cst_Game

   
class cst_Menu(DirectObject): 
    
    def __init__(self, parent):      
        self.root = parent
		        
        self.environ = loader.loadModel("data/models/env")
        self.environ.reparentTo(render)
        self.environ.setScale(0.25)
        self.environ.setPos(5, 25, 1)
        
        taskMgr.add(self.spinCameraTask, "SpinCameraTask")
		        
        self.main = cst_MenuMain(self)
        self.new = cst_MenuNew(self)
        self.options = cst_MenuOptions(self)
        
        self.credits = cst_MenuCredits(self)
    	self.accept("escape", exit)

    def spinCameraTask(self, task):
        angleDegrees = task.time * 2.0
        angleRadians = angleDegrees * (pi / 180.0)
        camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def cleanAll(self):
        taskMgr.remove('SpinCameraTask')
        self.environ.removeNode()

        self.new.__del__()
        self.options.__del__()
        self.credits.__del__()
        self.main.__del__()

    def startGame(self, BrainsList):
        self.cleanAll()
        print "Starting game with "
        print BrainsList
        print "..."
        self.root.startGame(BrainsList)
        
#
#   Main menu class
#
class cst_MenuMain(cst_GuiBox):
    def __init__(self, parent): 
        #                  Color                  Size                      Position                                    
        cst_GuiBox.__init__(self, (0, 0, 0, 0.5), (-0.43, 0.43, -0.44, 0.3), (-0.7, 0, -0.2))
        
        self.b.append(self.addButton("New Game", 0, 0.10, self.doAction, [parent, "new"]))
        self.b.append(self.addButton("Options", 0, -0.02, self.doAction, [parent, "options"]))
        self.b.append(self.addButton("Credits", 0, -0.14, self.doAction, [parent, "credits"]))
        self.b.append(self.addButton("Exit", 0, -0.26, self.doAction, [parent, "exit"]))

        self.show()
        
    def doAction(self, parent, action):
        self.hideAn()
        if (action == "new"): parent.new.showAn()
        elif (action == "options"): parent.options.showAn()
        elif (action == "credits"): parent.credits.showAn()
        elif (action == "exit"): 
            parent.cleanAll()
            exit()
        



#
#   New game menu class
#
class cst_MenuNew(cst_GuiBox):
    def __init__(self, parent):        
        #                  Color                  Size                    Position                                    
        cst_GuiBox.__init__(self, (0, 0, 0, 0.5), (-0.9, 0.9, -0.9, 0.9), (0, 0, 0))

        self.BrainsList = os.listdir(cst_FtConfig.BRAINS_PATH)
        self.LoadedBrainsList = []
        
        self.b.append(self.addButton("Back", -0.35, -0.7, self.b_back_action, [parent]))
        self.b.append(self.addButton("Waaarr!!!", 0.35, -0.7, self.b_start_action, [parent]))
      
        self.addText1("Select Desired Warriors:", -0.4, 0.7)
        
        self.Scroll = DirectScrolledFrame(pos = (-0.2, 0, 0.2),
                                          frameColor = (1, 1, 1, 0.7), 
                                          canvasSize = (-0.5,0.9,-0.7,0.4), 
                                          frameSize = (-0.5,0.9,-0.7,0.4),
                                          autoHideScrollBars = True) 
        self.Scroll.reparentTo(self.boxFrame)
        
        #todo
        #self.addRBList(self.Scroll, 0, 0, self.BrainsList)       

        self.hide()


    def b_addtank_action(self):
        return 0
          
    def b_back_action(self, parent):
        self.hideAn()    
        parent.main.showAn()

    def b_start_action(self, parent):
        parent.startGame(self.BrainsList)
         
 


#
#   Options menu class
#
class cst_MenuOptions(cst_GuiBox):
    def __init__(self, parent):    
        #                  Color                  Size                    Position                                    
        cst_GuiBox.__init__(self, (0, 0, 0, 0.5), (-0.7, 0.7, -0.7, 0.7), (0, 0, 0))

        self.addText1("Options menu", -0.4, 0.6)

        self.addText2("Resolution", 0, 0.3)
        self.b.append(self.addButton(str(cst_FtConfig.XRES) + "x" + str(cst_FtConfig.YRES), 0, 0.2, self.b_res_action, []))
        self.addText2("Fullscreen", 0, 0.05)
        self.b.append(self.addButton(cst_FtConfig.isFullScreen(), 0, -0.05, self.b_fscr_action, []))
        self.addText2("Sound", 0, -0.2)
        self.b.append(self.addButton(cst_FtConfig.isSound(), 0, -0.3, self.b_sound_action, []))
        self.b.append(self.addButton("Back", 0, -0.5, self.b_back_action, [parent]))

        self.hide()

    def b_res_action(self):
        cst_FtConfig.growRes()
        self.b[0]['text']=str(cst_FtConfig.XRES) + "x" + str(cst_FtConfig.YRES)
        return

    def b_fscr_action(self):
        cst_FtConfig.switchFullScreen();
        self.b[1]['text']=cst_FtConfig.isFullScreen()
        return

    def b_sound_action(self):
        cst_FtConfig.switchSound();
        self.b[2]['text']=cst_FtConfig.isSound()
        return

    def b_back_action(self, parent):
        self.hideAn()
        parent.main.showAn()
        return


#
#   Credits menu class
#
class cst_MenuCredits(cst_GuiBox):
    def __init__(self, parent):        
        #                  Color                  Size                    Position                                    
        cst_GuiBox.__init__(self, (0, 0, 0, 0.5), (-0.9, 0.9, -0.9, 0.9), (0, 0, 0))
        
        b_back = self.addButton("Back", 0, -0.7, self.b_back_action, [parent])

        self.hide()       

    def b_back_action(self, parent):
        self.hideAn()
        parent.main.showAn()
        return            


                
