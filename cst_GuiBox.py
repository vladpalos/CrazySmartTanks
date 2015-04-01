#
#  Crazy Smart Tanks Game 2011

#
#   description:    Common Menu Gui Functions/Objects
#   author:         Vlad Palos
#   date:           02.27.2011
#

        


from direct.gui.OnscreenText                import OnscreenText
from direct.gui.DirectGui                   import *
     
from direct.interval.IntervalGlobal         import * 


class cst_GuiBox:
    def __init__(self, color, size, position):
        self.bmap = loader.loadModel('data/models/gui/button1.egg')
        self.boxFrame = DirectFrame (frameColor = color, frameSize = size, pos = position)
        
        self.b = []

    def addText1(self, ptext, posx, posy):
        self.t = DirectLabel(text = ptext, text_fg = (1, 1, 1, 1), scale=0.07, relief = None, pos = (posx, 0, posy))
        self.t.reparentTo(self.boxFrame)      

    def addText2(self, ptext, posx, posy):
        self.t = DirectLabel(text = ptext, text_fg = (1, 0.7, 0.7, 0.7), scale=0.07, relief = None, pos = (posx, 0, posy))
        self.t.reparentTo(self.boxFrame)      

    
    def addButton(self, name, posx, posy, funct, args):        
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
        bt.reparentTo(self.boxFrame)   
        return bt


    def showAn(self):
        self.boxFrame.show()
        self.boxFrame.setScale(1.5)
        i  = self.boxFrame.colorScaleInterval(1, (1, 1, 1, 1), (1,1,1,0), blendType = 'easeOut')
        i2 = self.boxFrame.scaleInterval(0.5, 1, blendType='easeOut')         
        Sequence (
            Parallel(i, i2),
            Func(self.show)
        ).start()

        
    def hideAn(self):
        for x in self.b : x["state"] = DGG.DISABLED
# Animation Type 1
        self.pos = self.boxFrame.getPos();
        i  = self.boxFrame.colorScaleInterval(0.5, (1,1,1,0), blendType = 'easeOut')
        i2 = self.boxFrame.posInterval(0.5, (1, 0, 0), blendType='easeIn')         
        i3 = self.boxFrame.hprInterval(0.5, (0, 0, 40), blendType='easeIn')         
        Sequence (
            Parallel(i, i2, i3),
            Func(self.boxFrame.hide),
            Func(self.boxFrame.setHpr, (0, 0, 0)), 
            Func(self.boxFrame.setPos, self.pos) 
        ).start() 
# Animation Type 2
#        i  = self.boxFrame.colorScaleInterval(1, (1,1,1,0), blendType = 'easeIn')
#        i2 = self.boxFrame.scaleInterval(1, 50, blendType='easeIn')
#        Sequence (
#            Parallel(i, i2),
#            Func(self.boxFrame.hide),
#            Func(self.boxFrame.setScale, 1) 
#        ).start() 

        
    def show(self):
        for x in self.b : x["state"] = DGG.NORMAL
        self.boxFrame.show()       
               
               
    def hide(self):
        for x in self.b : x["state"] = DGG.DISABLED
        self.boxFrame.hide()       

        
    def __del__(self):
        self.boxFrame.destroy()
                


        
        
        
