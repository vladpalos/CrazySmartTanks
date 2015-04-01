#
#  Crazy Smart Tanks Game 2011

#
#   description:    Tank Instance/Functions Class 
#                   (inherits the Virtual Machine Class)
#   author:         Vlad Palos
#   date:           07.03.2011
#

        
##
##                     ----------------------------------TopNode----------------------------
##                     |                                    |                              |
##                 Tank Model                           Tank info                       Bullets
##                 |       |                                |                              |
##           ------         ------------                    .                      Bullets Collision
##          |                           |                                            |     |     | 
##       TankBase                 TankCollision                                      .     .     .
##          |                       |   |   |
##       TankTop                    .   .   .
##

from panda3d.core                           import *
from direct.gui.OnscreenText                import OnscreenText 
from direct.interval.IntervalGlobal         import *
import math

import cst_FtTools

from cst_TankTypes                          import *
from cst_VirtualMachine                     import cst_VirtualMachine
from cst_Ammo                               import cst_Ammo



class cst_Tank (cst_VirtualMachine):

    global TankType        

    def __init__(self, 
                parent, count, brain, team, t,
                xpos, ypos):
     
        cst_VirtualMachine.__init__(self, brain)
        

        tname = "Tank_" + str(count)

        ## Basic       
        self.isDead = False

        self.parent = parent
        self.team = team
        self.tankName = brain[0:-3]
        self.health = 100
        self.brain = brain
        self.count = count    

        self.weight = TankType[t] ['weight']
        self.rrange = TankType[t] ['rrange']
        self.scaleFactor = TankType[t] ['scale']

        self.tankTypeAmmo = TankType[t] ['ammo']

        collisions =  TankType[t] ['coll']
        model =  TankType[t] ['model']


        self.speed = 0  
        self.rot = 0  
        
        self.mW = 40.0 # Tanks medium weight

        self.rotStep = ( 2.0 * globalClock.getDt() / float ( self.weight * 4 ) ) * self.mW
        self.speedStep = (0.2 * self.mW * globalClock.getDt()) / float(self.weight)

        self.xpos = xpos
        self.ypos = ypos
 

        ## Top Node
        self.TopNode = NodePath ( tname )
        self.TopNode.reparentTo( render )

        self.TopNode.setTag('count', str (count))

        ## Tank model node
        self.TankModel = NodePath( tname + "_model" )
        self.TankModel.reparentTo( self.TopNode )


        if (TankType[t]['parts'] == 1):            
            ## Tank Model
            self.TankBaseModel = loader.loadModel(model)
            self.TankBaseModel.reparentTo ( self.TankModel )
            
        if (TankType[t]['parts'] == 2):
            ## Tank Base
            self.TankBaseModel = loader.loadModel("data/models/Players/"+model+"/base.egg")
            self.TankBaseModel.reparentTo ( self.TankModel )

            ## Tank Top
            self.TankTopModel = loader.loadModel("data/models/Players/"+model+"/top.egg")
            self.TankTopModel.reparentTo ( self.TankBaseModel )

        ## Initial Transformations        
        self.TopNode.setPos( self.xpos , self.ypos, 0 )
        self.TopNode.setScale( self.scaleFactor )
   
        ## Info Node
        self.textNode = OnscreenText(text=self.infoText(), 
                                     fg=(1,0.2,0.1,1),
                                     pos=(10,0),
                                     scale=.04,
                                     mayChange=1) 
        self.textNode.setFont( parent.font1 )
        
        ## Collisions
        ## Poor Collision References
        ## Shoud define Collision points in .egg file ( via 3d modeling program )
        self.collNode = self.TankModel.attachNewNode( CollisionNode( "tank" ) )

        for x in range ( 0, len ( collisions ) , 2 )  :
            self.collNode.node().addSolid( CollisionSphere( collisions[x], collisions[x+1] ) )        

        parent.pusher.addCollider( self.collNode, self.TopNode )
        base.cTrav.addCollider(self.collNode , parent.pusher)
        
        
        self.ammo = cst_Ammo(self, count, t, xpos, ypos )
        
        ## Tank Explosion

        expModel = loader.loadModel( TankType[t]['explosion_model'])
        expModel.setScale ( TankType[t]['explosion_scale'] )
        expModel.node().setEffect (BillboardEffect.makePointEye())                    

        self.expNode = render.attachNewNode( "exp_" + str( count ))  
        expModel.reparentTo ( self.expNode )
        self.expNode.hide()

        exSound = loader.loadSfx(TankType[t]['explosion_sound'])
#        print (TankType[t])
#        hitSound = loader.loadSfx(TankType[t]['hit_sound'])
                                               
        self.exSoundInt = SoundInterval( exSound, loop = 0 ) 
 #       self.hitSoundInt = SoundInterval( hitSound, loop = 0 ) 

#####################################################################################################         

    def setHealth(self, x):
        if ( x <  0 ):   
            self.health = self.health + x
        else :
            self.health = x
                
  #      self.hitSoundInt.start()
        self.textNode.setText(self.infoText())

    def setSpeed (self,x):
        if ( x < 100 ):
            if ( x < 0 ): 
                self.speed = 0
            else :
                self.speed = x
        else: 
            self.speed = 100

    def infoText(self):
        s = ''
        if (self.team == 1):
            s = '*'
        if (self.team == 2):
            s = '$'
        return self.tankName + " " + s + " " + "\n" + str ( self.health ) 

    def stateTask(self, task):
        
        ## Is dead ? 
        if ( self.health <= 0 ):            
            self.die()
            return task.done
        else :
            ## Speed
            if ( self.speed > 0 ):
                sp = ( self.speed / 100.0 )
                self.TopNode.setX(self.TopNode, ( sp * self.speedStep ) )
                self.xpos = self.TopNode.getX()
                self.ypos = self.TopNode.getY()

        
            ## Rotation
            if (self.rot != 0 ):

                if (self.rot < 0 ) : rs = self.rotStep
                else : rs = -self.rotStep

                new = self.rot + rs

                if (( new < 0 and self.rot > 0 ) or (new > 0 and self.rot < 0)):                
                    self.rot = 0
                else :
                    self.rot = new
                    self.TopNode.setH(self.TopNode, rs)                 

            ## Tank Info Update
            pos = cst_FtTools.map3dToAspect2d( render , self.TopNode.getPos() )

            if ( pos == None ) :
               self.textNode.hide()
            else:
               self.textNode.show()
               self.textNode['pos']=( pos[0] + 0.1 , pos[2] + 0.1 ) 
                
            return task.cont
    
    def die(self):
    
        self.isDead = True 
        
        self.TopNode.removeNode()
        self.textNode.removeNode()
        taskMgr.remove ('tank_task_state_'+str(self.count))
        taskMgr.remove ('tank_task_run_'+str(self.count))

        self.expNode.setPos(self.xpos, self.ypos, 5)
        self.expNode.show()
        p = self.expNode.find('**/+SequenceNode').node().play
        Sequence( Parallel ( Func ( p , 0, 16 ) ,  self.exSoundInt), 
                  Func ( self.expNode.removeNode ) ).start()
    
#####################################################################################################         

    ## Allowed Callback functions
    code_funct = [
              'drive', 'stop', 'scan', 'shoot', 'damage', 
              'getspeed', 'loc_x', 'loc_y', 'rand', 
              'sqrt', 'sin', 'cos', 'tan', 'atan',
              'talk', 'rotate', 'loc_nx', 'loc_ny', 
              'drive_to'
              ]


    ## Functions

    def talk(self, string):
        print string        

    def go(self, x, y):
        pass

    def loc_nx(self):
        return 0
    
    def loc_ny(self):
        return 0

    def drive(self, speed):
        if (speed > 100): self.speed = 100
        else : self.speed = speed

    def drive_to(self, speed, x, y):
        if (speed > 100): self.speed = 100
        else : self.speed = speed

        tx = self.xpos
        ty = self.ypos
        v1 = Vec3(tx, ty, 0)
        v2 = Vec3(x - tx , y - ty, 0)        
        v1.normalize();
        v2.normalize();
        
        print  (v1.angleDeg(v2))
        
        self.rotate( v1.angleDeg(v2) )

        
    def stop(self):
        self.speed = 0
        
    def rotate( self, angle ):
        if (angle > 360 or angle < -360):
             angle = angle % 360
        self.rot = angle

    def scan(self):
        r = self.rrange**2
        m = -1

        for x in range ( self.parent.tanksCount ) :
            p1 = (self.parent.tanks[x].xpos, self.xpos)
            p2 = (self.parent.tanks[x].ypos, self.ypos)

            d =  cst_FtTools.distSq( p1, p2 )
            if ( d < r ):
                if ( m == - 1):
                    m = x
                else :                    
                    if ( d <  cst_FtTools.distSq( (self.parent.tanks[m].xpos, self.xpos), (self.parent.tanks[m].ypos, self.ypos) ) ):
                        m = x
        if ( m != -1 ):
            p1 = (self.parent.tanks[m].xpos, self.xpos)
            p2 = (self.parent.tanks[m].ypos, self.ypos)
            return math.sqrt ( cst_FtTools.distSq( p1, p2 ) )
        else : return -1     


            

    def shoot(self, x, y):
        if (x <= self.parent.mapW and  x >= (-self.parent.mapW) and
            y <= self.parent.mapH and  y >= (-self.parent.mapH)):

            self.ammo.add_bullet(x, y)

            sc = str(self.count)
            taskMgr.remove("tank_task_run_" + sc)
            taskMgr.doMethodLater(self.tankTypeAmmo['ctime'], self.run, 'tank_task_run_'+ sc, taskChain= 'tank_task_chain_' + sc)
            

    def health(self):  
        return self.health
        
    def getspeed(self):
        return int ( self.speed ) 
        
    def loc_x(self):                            
        return int ( self.xpos )
        
    def loc_y(self):                            
        return int ( self.ypos )
        
    def rand(self, x, y):
        return random.uniform (x, y)
        
    def sqrt(self, x):                
        return math.sqrt(x)
        
    def sin(self, x):       
        return math.sin(x)
        
    def cos(self):                              
        return math.cos(x)
        
    def tan(self,x):       
        return math.tan(x)
        
    def atan(self):                             
        return math.atan(x)

