#
#  Crazy Smart Tanks Game 2011

#
#   description:    CST Main game class
#   author:         Vlad Palos
#   date:           05.03.2011
#

        

from panda3d.core                               import *

from direct.showbase.DirectObject               import DirectObject
from direct.task                                import Task    
from direct.gui.OnscreenText                    import OnscreenText 
from direct.gui.OnscreenImage                   import OnscreenImage
from pandac.PandaModules                    	import Vec3

import random


import cst_FtConfig
from cst_Tank                                   import cst_Tank     
from cst_Scene                                  import cst_Scene     

class cst_Game(DirectObject):

    def __init__(self, rP, t):

        self.root = rP

        print "Initializig Game..."
        if Thread.isThreadingSupported() : 
            print "Threading supported ..."
        else :
            print "Please compile panda3d with Threading support !"
            exit ()

        # Check video card capabilities.
        if (base.win.getGsg().getSupportsBasicShaders() == 0):
            print "Glow Filter: Video driver reports that shaders are not supported."
            exit()



        self.tanksCount = len(t)
        self.tanks = []
        self.mapW = 50 # Half the size
        self.mapH = 50
        self.worldB = -63
        self.worldT = 70
        self.worldL = -65 
        self.worldR = 65

        self.font1 = loader.loadFont('data/Fonts/capture2.ttf')
        self.font2 = loader.loadFont('data/Fonts/Allegro.ttf')
    
        self.setupCollisionDetection()
        self.createScene()	
        self.setEvents()
        
        taskMgr.add(self.gameCheckTask, "game_check_task")

        ## Adding tanks | Shared Memory

        for x in range(self.tanksCount):    
            self.tanks.append(  cst_Tank(self, x, t[x]['brain'],t[x]['team'], t[x]['type'] ,
                                random.uniform(0, 0)+((1-x)*10), random.uniform(0, 0)))

        print "Running..."


        ## Fore each Tank a Task Chain in created
        ##
        ## Then the Tank's run method is added to the task manager.
        ## The method executes only one line of brain code per frame. 
        ## When there is no code left, the task is terminated.

        for x in range(0, self.tanksCount):    

            taskMgr.setupTaskChain('tank_task_chain_'+str(x), 
                                    numThreads = 1, 
                                    timeslicePriority = False, 
                                    threadPriority = 0, 
                                    frameSync = True )
            taskMgr.add(self.tanks[x].run, 'tank_task_run_'+str(x),taskChain= 'tank_task_chain_' + str(x))
            taskMgr.add(self.tanks[x].stateTask, 'tank_task_state_'+str(x),taskChain= 'tank_task_chain_' + str(x))

    
#        base.cTrav.showCollisions( render )

    def createScene(self):

        ## Setting the camera
        base.camera.setPos(0, -160, 80)
        base.camera.lookAt(0, 50, -50)

        ## Disable basic camera mouse movements from directStart
        base.disableMouse()        
        taskMgr.add(self.mouseCameraTask, "move_mouse_camera")
      
        ## Load Ground      
        self.ground = render.attachNewNode(CollisionNode("ground"))
        self.ground.node().addSolid(CollisionPlane(Plane(Vec3(0, 0, 1),Point3(0, 0, 0))))

        self.cm = CardMaker("ground_cm")
        self.cm.setFrame(self.worldL, self.worldR, self.worldB, self.worldT)
        self.ground = render.attachNewNode(self.cm.generate())
        tex = loader.loadTexture('data/models/maps/ground1.png')
        self.ground.setTexture ( tex )
        self.ground.setTwoSided(True)
        self.ground.setPos(0, 0, 0)
        self.ground.lookAt(0, 0, -1)

        ## Load Invisible Walls
        self.wallE = render.attachNewNode(CollisionNode("wall"))
        self.wallE.node().addSolid(CollisionPlane(Plane(Vec3(-1, 0, 0),Point3(self.mapW, 0, 0))))

        self.wallN = render.attachNewNode(CollisionNode("wall"))
        self.wallN.node().addSolid(CollisionPlane(Plane(Vec3(1, 0, 0),Point3(-self.mapW, 0, 0))))

        self.wallW = render.attachNewNode(CollisionNode("wall"))
        self.wallW.node().addSolid(CollisionPlane(Plane(Vec3(0, -1, 0),Point3(0, self.mapW, 0))))

        self.wallS = render.attachNewNode(CollisionNode("wall"))
        self.wallS.node().addSolid(CollisionPlane(Plane(Vec3(0, 1, 0),Point3(0, -self.mapW, 0))))


        cst_Scene( self )
        
        
    def setupCollisionDetection(self):

        base.cTrav = CollisionTraverser()

        self.pusher = CollisionHandlerPusher()
        self.pusher.addInPattern("%fn-in-%in")
        self.pusher.addOutPattern("%fn-out-%in")

        self.accept("tank-in-tank", self.onTankInTank)
        self.accept("tank-out-tank", self.onTankOutTank)

        self.accept("tank-in-wall", self.onTankInWall)
        self.accept("tank-out-wall", self.onTankOutWall)

        self.accept("tank-in-bullet", self.onTankInBullet)
        self.accept("tank-out-bullet", self.onTankOutBullet)


    def onTankInBullet(self, entry):
#        btc = int ( entry.getIntoNodePath().getNetTag('fromtank') )
#        bt = int ( entry.getIntoNodePath().getNetTag('type') )
        bd = int ( entry.getIntoNodePath().getNetTag('damage') )
#        bc = int ( entry.getIntoNodePath().getNetTag('count') )

        tc = int ( entry.getFromNodePath().getNetTag('count') )        
        
        self.tanks[tc].setHealth( -bd )

    def onTankOutBullet(self, entry):
        pass        

    def onTankInWall(self, entry):
        tc = int ( entry.getFromNodePath().getNetTag('count') )        
        
        self.tanks[tc].setSpeed( 0 )
        self.tanks[tc].setHealth( -1 )
        
        
    def onTankOutWall(self, entry):
        pass

    def onTankInTank(self, entry):
        bc = int ( entry.getIntoNodePath().getNetTag('count') )
        tc = int ( entry.getFromNodePath().getNetTag('count') )        
        
        self.tanks[tc].setHealth( -0.1 )
        self.tanks[bc].setHealth( -0.1 )

    def onTankOutTank(self, entry):
        pass

    def setEvents(self):
        self.accept("pause-game", self.pauseGame)    
        self.accept("escape", self.endGame)

    def mouseCameraTask(self, task):
        if base.mouseWatcherNode.hasMouse():
            x = base.mouseWatcherNode.getMouseX() 
            y = base.mouseWatcherNode.getMouseY() 

            x = x * 10
            y = y * 10 
                
            if ( x > -10 and x < 10 ):            
                base.camera.setX(x)                

            if ( y > -10 and y < 10 ):            
                base.camera.setY(y - 140)                
        return task.cont

    def pauseGame (self, what, text):
    # Alpha
    
#        for x in taskMgr.getAllTasks():
#            print dir (x) 
 #           print "============================================"
        
        img = OnscreenImage(parent=render2d, image="data/models/maps/game_won.png")
        self.textNode = OnscreenText(parent = render2d,
                                     text="Team # Won !!! \n\n\n Good Game !\n\n\n\nPress enter to exit", 
                                     fg=(1,1,1,1),
                                     pos=(0,0.1),
                                     scale=.04,
                                     mayChange=1) 
        self.textNode.setFont( self.font2 )    
        self.textNode.setBin("fixed", 160)   
                                     
        img.setScale (0.3)
        img.setTransparency(TransparencyAttrib.MAlpha)
       
        self.accept ("enter", self.endGame)
            
            

    def gameCheckTask (self, task):
        tm = -1
        for i in range (self.tanksCount):
    
            if ( self.tanks[i].isDead == False):
                if (tm == -1):
                    tm = self.tanks[i].team
                else :
                    if (tm != self.tanks[i].team ):
                        return task.cont
        
        if (tm != -1):
            messenger.send("pause-game",["gamewon", str(tm)])
            return task.cont

        if (tm == -1):
            messenger.send("pause-game",["gamewon", "ERROR"])
            return task.cont
                        

    def endGame(self):
        
        print "Deinitializing Game..."
        print "..."
        exit()
		
