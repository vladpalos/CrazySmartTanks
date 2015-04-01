#
#  Crazy Smart Tanks Game 2011

#
#   description:    CST - Main Class
#   author:         Vlad Palos
#   date:           02.02.2011
#


####DEBUG####
#from pandac.PandaModules import loadPrcFileData
#loadPrcFileData("", "want-directtools t")
#loadPrcFileData("", "want-tk t")
############

import direct.directbase.DirectStart

import cst_FtConfig
import os

from cst_Menu                               import cst_Menu
from cst_Game                               import cst_Game


class cst_App:    
    def __init__(self):   

        cst_FtConfig.setup()
    #    cst_FtConfig.showDebug()        

        self.startMenu()

    def startMenu(self):
        cst_Menu(self)

    def startGame(self, tankBrains):

        tanks = []
        i = 0
        for tbn in tankBrains:
            tanks.append(dict)
            tanks[i] = {}
            tanks[i]['brain'] = str(tbn)
            tanks[i]['team'] = int ( tankBrains[tbn]['Team'] ) 
            tanks[i]['type'] = int ( tankBrains[tbn]['Tank'] ) - 1
            i = i + 1;
     
        """          
        print "---------"
       
        t = []

        t.append( dict )
        t[0] = {}
        t[0]['brain'] = 'cute.tb'
        t[0]['type'] = 0
        t[0]['team'] = 1

        t.append(dict)
        t[1] = {}
        t[1]['brain'] = 'terminator.tb'
        t[1]['type'] = 1
        t[1]['team'] = 2

        print tanks
        print t
   
        print len(tanks)
        print len(t)
        """
        cst_Game(self,tanks)        
                
Appl = cst_App()
run()

#  or for external 3rd party Python user events or such
## from twisted.internet.task import LoopingCall
## from twisted.internet import reactor
 
## LoopingCall(taskMgr.step).start(1 / Desired_FPS)
## reactor.run()
