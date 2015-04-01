#
#  Crazy Smart Tanks Game 2011

#
#   description:    Menu 
#   author:         Vlad Palos, Valcea Valentin
#   date:           05.03.2011
#


import cst_FtConfig

import os
from math                                       import pi, sin, cos

from direct.task                                import Task    
from direct.gui.DirectGui                       import *
from pandac.PandaModules                        import *

from cst_GuiBox                                 import cst_GuiBox
from cst_Game                                   import cst_Game

class cst_Menu(): 
    
    def __init__(self, parent):      
        self.root = parent
        
        self.environ = loader.loadModel("models/environment")
        self.environ.reparentTo(render)
        self.environ.setScale(0.25)
        self.environ.setPos(5, 25, 1)
        taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        
        self.main = cst_MenuMain(self)
        self.new = cst_MenuNewGui(self)
        self.options = cst_MenuOptions(self)
        self.help = cst_MenuHelp(self)

               
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
        self.help.__del__()
        self.main.__del__()
    

    def startGame(self, BrainsList):
        self.cleanAll()
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
        self.b.append(self.addButton("Help", 0, -0.14, self.doAction, [parent, "help"]))
        self.b.append(self.addButton("Exit", 0, -0.26, self.doAction, [parent, "exit"]))

        self.show()
        
    def doAction(self, parent, action):
        self.hideAn()
        if (action == "new"): parent.new.showAn()
        elif (action == "options"): parent.options.showAn()
        elif (action == "help"): parent.help.showAn()
        elif (action == "exit"): 
            parent.cleanAll()
            exit()
        

#
#   New game menu class
#

class cst_MenuNewGui(cst_GuiBox):
    def __init__(self, parent):
        
        #                  Color                  Size                    Position                                    
        cst_GuiBox.__init__(self, (0, 0, 0, 0.5), (-0.99, 0.99, -0.99, 0.99), (0, 0, 0))
        
        self.parent = parent

        self.BrainsList = os.listdir(cst_FtConfig.BRAINS_PATH)
        self.loadedBrains = {}
        
        self.setScrollFrame(-0.4, 0.3, 0.2, 0.25, 0.2, -0.85)
        self.makeList(self.BrainsList)    
        
        self.setScrollFrame(0.4, 0.3, 0.2, 0.25, 0.2, -0.85)
            
        self.b.append(self.addButton("Back", -0.35, -0.7, self.b_back_action, [parent]))
        self.b.append(self.addButton("Next", 0.35, -0.7, self.b_next_action, [parent]))
      
        self.addText1("Select Desired Warriors:", -0.4, 0.7)
        
        self.hide()

    def setScrollFrame(self, posx, posy, decButton_posx, decButton_posy, incButton_posx, incButton_posy):
        #scroll list define
        self.numItemsVisible = 7
        self.itemHeight = 0.11
        self.scrollFrameList = DirectScrolledList(  decButton_pos= (decButton_posx, 0, decButton_posy),
                                                    decButton_text = "Up",
                                                    decButton_text_scale = 0.06,
                                                    decButton_borderWidth = (0.005, 0.005),
                                                 
                                                    incButton_pos= (incButton_posx, 0, incButton_posy),
                                                    incButton_text = "Down",
                                                    incButton_text_scale = 0.06,
                                                    incButton_borderWidth = (0.005, 0.005),
                                                 
                                                    frameSize = (-0.3, 0.3, -0.75, 0.2),
                                                    frameColor = (1, 1, 1, 0.3),
                                                    pos = (posx, 0, posy),
                                                    numItemsVisible = self.numItemsVisible,
                                                    forceHeight = self.itemHeight  )
        self.scrollFrameList.reparentTo(self.boxFrame)

    #does scrolled list
    def makeList(self, list):
        posy = 0.29
        brainListScroll = []
        for tankb in list:
            brainListScroll.append(self.addButtonScroll(tankb, 0.15, posy, self.b_add_action, [tankb, posy]))
            posy = posy - 0.10


    def b_add_action(self, name, posy):
        if ( name not in self.loadedBrains ):
            
            dict = {name : self.addButtonScroll(name, 0.15, posy, self.b_add_action_delete, [name])}
            self.loadedBrains.update(dict)
            
        
    def b_add_action_delete(self, name):
        if self.loadedBrains.has_key(name):
            del self.loadedBrains[name]
            self.scrollFrameList.removeAndDestroyAllItems()
            posy = 0.29
            brainListScroll = []
            for tankb in self.loadedBrains:
                brainListScroll.append(self.addButtonScroll(tankb, 0.15, posy, self.b_add_action_delete, [tankb]))
                posy = posy - 0.10
        
    #add tank to loaded tanks list and prints the list with all tanks added and open cst_MenuTankConfig
    def b_next_action(self, name):
        if (len(self.loadedBrains)>1):
            self.hideAn()
            self.mtc = cst_MenuTankConfig(self)
            self.loadedBrains = self.mtc.tankSave

          
    def b_back_action(self, parent):
        self.hideAn()    
        parent.main.showAn()

        
    def b_start_action(self, parent):
        parent.startGame(self.loadedBrains)
    
    def addButtonScroll(self, name, posx, posy, funct, args):        
        bt = DirectButton(
                        text = name,
                        text_fg = (1, 1, 1, 1),
                        scale = 0.07,
                        geom_scale = 3,
                        geom_pos = (0, 0, 0.3),                        
                        pos = (posx, 0, posy),
                        relief = None,
                        command = funct,
                        extraArgs = args,
                        textMayChange = 1, 
                        geom = (self.bmap.find('**/button1_ready'),
                                self.bmap.find('**/button1_click'),
                                self.bmap.find('**/button1_rollover'),
                                self.bmap.find('**/button1_disabled')))
        
        self.scrollFrameList.addItem(bt)   
        return bt

###
### CLASS FOR TANK CONFIGURATION GUI
###
class cst_MenuTankConfig(cst_GuiBox):
    def __init__(self, parent):
   
        cst_GuiBox.__init__(self, (0, 0, 0, 0.7), (-0.7, 0.7, -0.7, 0.7), (0, 0, 0))
        # select all types of tanks
        self.tankType = ["Select", "1", "2", "3", "4"]

        self.tank = []
       # for i in range(0, len(parent.loadedBrains)):
        #    self.tank.insert(i, self.tankType[0])
            
        self.TEAM = ["Select"]
        for i in range(1, len(parent.loadedBrains) + 1):
            self.TEAM.insert(i, str(i))
         
        self.team = []
        self.lastTank = None
        self.name = []
        self.tankSave = {}
        self.count = 0
        
        for i in parent.loadedBrains:
            dict = {i : '0'}
            self.tankSave.update(dict)
            self.name.append(i)
        
                      
        # lists for capting text
        self.text = []
        
        # list for textAreas
        self.listArea = []
        
        self.setScrollFrame(-0.2, 0.4, 0.6, 0.2, 0.6, -0.8)
        # fill the scrollFrame
        self.makeList(parent.loadedBrains)        
        
        # save button
        self.addButton("Fight", -0.4, -0.6, self.b_start_action, [parent])
        # view button
        self.addButton("Tanks", 0.4, -0.6, self.b_view_action, [parent])
        
    # create scroll frame
    def setScrollFrame(self, posx, posy, decButton_posx, decButton_posy, incButton_posx, incButton_posy):
        #scroll list define
        numItemsVisible = 7
        itemHeight = 0.11
        self.scrollFrameList = DirectScrolledList(
                                                    decButton_pos= (decButton_posx, 0, decButton_posy),
                                                    decButton_text = "Up",
                                                    decButton_text_scale = 0.06,
                                                    decButton_borderWidth = (0.005, 0.005),
                                                 
                                                    incButton_pos= (incButton_posx, 0, incButton_posy),
                                                    incButton_text = "Down",
                                                    incButton_text_scale = 0.06,
                                                    incButton_borderWidth = (0.005, 0.007),
                                                 
                                                    frameSize = (0, 0, 0, 0),
                                                    frameColor = (0, 0, 0, 0.5),
                                                    pos = (posx, 0, posy),
                                                    numItemsVisible = numItemsVisible,
                                                    forceHeight = itemHeight,
                                                    
                                                    #itemFrame_frameSize = (-0.5, 0.5, -0.5, 0.5),
                                                    #itemFrame_pos = (0, 0, 0),
                                                    #itemFrame_frameColor = (1, 0, 0, 0.7)
                                                    )
        self.scrollFrameList.reparentTo(self.boxFrame)

    def makeList(self, parentList):
        pos_y = 0.55
        for i in parentList:
            self.setTextOnScreen(text = "-----------------------")
            self.setTextOnScreen(text = "Name:") 
            self.setTextOnScreen(text = i)
            self.setTextOnScreen(text = "Team:")
            #self.doTextArea(text = "Team:", posx = -0.3, posy = pos_y)
            self.doMenuOption2(self.TEAM, posx = -0.3, posy = pos_y)
            self.setTextOnScreen(text = "Type:")
            self.doMenuOption1(self.tankType, posx = 0.5, posy =  pos_y)
            pos_y = pos_y - 0.20
        
    
    def doTextArea(self, text, posx, posy):
        self.setTextOnScreen(text)
        
        self.textArea = DirectEntry(text = "" , scale=0.05, command = self.getText,
                               pos = (posx + 0.10, 0, posy),
                               initialText="", numLines = 1, focus=1,
                               focusInCommand = self.clearText) 
        self.textArea.reparentTo(self.scrollFrameList)
        
        self.scrollFrameList.addItem(self.textArea)
        self.listArea.append(self.textArea)

    def setTextOnScreen(self, text):
        textNode = TextNode(text)
        textNode.setText(text)
        textNode.setTextColor(1, 1, 1, 1)
        textNode = aspect2d.attachNewNode(textNode)
        textNode.setScale(0.05)
        self.scrollFrameList.addItem(textNode)
        
        
    #get the text from the textArea after pressing ENTER and append it to 'text' list            
    def getText(self, textEntered):
        self.text.append(textEntered)
        #print self.text

    #after b_back shows all text entered from all textAreas
    def getAllText(self):
        i = 0
        for it in self.listArea:
            self.team.append(it.get())
            i = i + 1
        self.setSetupList()


    #do menu
    def doMenuOption1(self, items, posx, posy):
        menu = DirectOptionMenu(text="Tank type", scale=0.08, items = items,
                                pos = (posx, 0, posy),
                                initialitem = 0,
                                highlightColor = (0.65,0.65,0.65,1),
                                command = self.itemSelect1,
                                textMayChange = 1)
        #menu.reparentTo(self.scrollFrameList)
        self.scrollFrameList.addItem(menu)
    
    def doMenuOption2(self, items, posx, posy):
        menu = DirectOptionMenu(text="Tank type", scale=0.08, items = items,
                                pos = (posx, 0, posy),
                                initialitem = 0,
                                highlightColor = (0.65,0.65,0.65,1),
                                command = self.itemSelect2,
                                textMayChange = 1)
        #menu.reparentTo(self.scrollFrameList)
        self.scrollFrameList.addItem(menu)
    
        
    # selects an item form menuOption
    def itemSelect1(self, arg):
        self.tank.append(str(arg))
        """
        aux = []
        start = len(self.tank) - len(self.listArea) 
        end = len(self.tank) 
        
        if len(self.tank) > len(self.listArea):
            for i in range(start, end):
                aux.append(self.tank[i])
                
        if len(aux) == len(self.listArea):
            self.tank = aux
        """

    
    # selects an item form menuOption
    def itemSelect2(self, arg):
        self.team.append(str(arg))
        
        
    #do setup list    
    def setSetupList(self):

        if len(self.tankSave) > 0 and len(self.team) > 0 and len(self.tank) > 0 :
            i = 0
            for name in self.tankSave :
                if (self.team[i] == 'Select'):
                    self.team[i]=1
                if (self.tank[i] == 'Select'):
                    self.tank[i]=1
                self.tankSave[name] = {'Team' : self.team[i], 'Tank' : self.tank[i]}
                i = i + 1
            
            
    #clear text after focus or pressing ENTER key     
    def clearText(self):
        self.textArea.enterText('')
        
    # go back action button
    def b_start_action(self, parent):
        #self.getAllText()
        if len(self.tankSave) > 0 and len(self.team) >= len(self.tankSave) and len(self.tank) >= len(self.tankSave) :
            self.setSetupList()
            self.hideAn()    
            parent.b_start_action(parent.parent)

    def b_view_action(self, parent):
        self.hideAn()
        self.mtt = cst_MenuTankType(self)
        
#
# class for view the thank type; just a picture
#
class cst_MenuTankType(cst_GuiBox):
    def __init__(self, parent):
        cst_GuiBox.__init__(self, (0, 0, 0, 0.7), (-0.9, 0.9, -0.9, 0.9), (0, 0, 0))

        self.image = OnscreenImage("data/images/TanksInfo.jpg", pos = (0, 0, 0), scale = 0.4)
        self.image.reparentTo(self.boxFrame)
        
        self.addButton("Back", -0.6, -0.6, self.b_back_action, [parent])
        
    def b_back_action(self, parent):
        self.__del__()
        parent.showAn()
        
    def __del__(self):
        self.boxFrame.destroy()
        
            
         

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
#   help menu class
#

class cst_MenuHelp(cst_GuiBox):
    def __init__(self, parent):        
        #                  Color                  Size                    Position                                    
        cst_GuiBox.__init__(self, (0, 0, 0, 0.5), (-0.9, 0.9, -0.9, 0.9), (0, 0, 0))

        self.setTextOnScreen(text = "Vlad Palos", posx = 0, posy = 0.4)    
        self.setTextOnScreen(text = "Valentin Valcea", posx = 0, posy = 0.2)
        self.setTextOnScreen(text = "Andreea Albuletu", posx = 0, posy = 0.0)
        self.setTextOnScreen(text = "Emil Pana", posx = 0, posy = -0.2)
        self.setTextOnScreen(text = "Victor Lacatusu", posx = 0, posy = -0.4)    
        
        b_back = self.addButton("Back", 0, -0.7, self.b_back_action, [parent])

        self.hide()       

    def setTextOnScreen(self, text, posx, posy):
        text = OnscreenText(text = text, pos = (posx, posy),fg = (1, 1, 1, 1))
        text.reparentTo(self.boxFrame)

    def b_back_action(self, parent):
        self.hideAn()
        parent.main.showAn()
        return            


                
