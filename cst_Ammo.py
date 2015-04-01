#
#  Crazy Smart Tanks Game 2011

#
#   description:    Bullets , gadgets and everything nice.
#   author:         Vlad Palos
#   date:           25.04.2011
#



from panda3d.core                           import *
from direct.interval.IntervalGlobal         import *
from direct.actor                           import Actor 

from cst_TankTypes                          import *
from cst_FtTools                            import *


class cst_Ammo ():

    global TankType

    def __init__(self,parent, tankCount, t, tankX, tankY):    
        
        self.parent = parent
        self.tX = tankX
        self.tY = tankY
        self.tcount = tankCount
        self.type = t
        self.ammoType = TankType[t]['ammo']    

        self.ammoSpeed = self.ammoType['speed']
        self.coll = self.ammoType['coll']

        ## Bullets / Gun
        self.ammoNode = NodePath ( "bulletNP" )
        self.ammoModel = loader.loadModel(self.ammoType['model'])
        if (self.ammoType['texture']!='none'):
            self.ammoModel.setTexture ( loader.loadTexture(self.ammoType['texture']) )
        self.ammoModel.setScale (self.ammoType['scale'])
        self.ammoModel.reparentTo( self.ammoNode )



        shSound = loader.loadSfx(self.ammoType['sound_shoot'])
        exSound = loader.loadSfx(self.ammoType['sound_explode'])

        self.shSoundInt = SoundInterval( shSound, loop = 0 ) 
        self.exSoundInt = SoundInterval( exSound, loop = 0 ) 
        
        self.bullets = []
        self.bulletsCN = []
        self.bulletInUse = []
        self.seq = []
        self.exp = []

        for count in range ( self.ammoType['load_bullets'] ) :
             
            np = render.attachNewNode( "bullet_" + str( count ))            
            np.setTag('type', str(self.type))
            np.setTag('fromtank', str(self.tcount))
            np.setTag('count', str(count))
            np.setTag('damage', str(self.ammoType['damage']))

            self.bullets.append( np ) 
            self.ammoNode.instanceTo(self.bullets[count])

            self.bullets[count].setPos(0, 0, 100)       
            
            self.bulletsCN.append( self.bullets[count].attachNewNode( CollisionNode( "bullet" ) ) )
            self.bulletsCN[count].node().addSolid( CollisionSphere( self.coll[0], self.coll[1] ) )        

            self.bullets[count].hide()

            self.bulletInUse.append ( False )
            self.seq.append ( None )
            
            ## Explosion
            expModel = loader.loadModel(self.ammoType['explosion_model'])
            expModel.setScale ( self.ammoType['explosion_scale'] )
            expModel.node().setEffect (BillboardEffect.makePointEye()) 
           
            np = render.attachNewNode( "exp_" + str( count ))  
            expModel.reparentTo ( np )
            np.hide()
            self.exp.append( np )
                 

    def add_bullet(self, x, y):
        
        for x in range ( len ( self.bulletInUse ) ):
            if (self.bulletInUse[x] == False):
                self.bulletInUse[x] = True
                self.bullets[x].show()
                self.bullets[x].setPos(self.tX, self.tY, self.ammoType['bulletZ'])       
    
                #Duration               
                dist =  distSq ( (x, self.tX), (y, self.tY))               
 
                d = 2.5      
#                d = ( dist / 20000 ) * self.ammoSpeed

                pint = ProjectileInterval(self.bullets[x],
                                          startPos = (self.parent.TopNode.getX(), self.parent.TopNode.getY(), self.ammoType['bulletZ']),
                                          endPos = Point3(x, y, 0), duration = d, gravityMult = 1 )

                self.shSoundInt.start()

                self.seq[x] = Sequence (  
                            pint,
                            Parallel (self.exSoundInt , Func (self.enableBullet, x), Func (self.vibCamera)), 
                            Func (self.exp[x].hide))
                self.seq[x].start()
                    
                break                

    def vibCamera(self):
        pass
#        base.camera.colorInterval(1, (1, 1, 1, 1))

    def enableBullet (self, x ):
        pos = self.bullets[x].getPos()        
        self.bullets[x].setPos(0, 0, 100)
        self.bullets[x].hide()

        self.exp[x].show()
        self.exp[x].setPos(pos + (0, 0, 5))
        self.exp[x].find('**/+SequenceNode').node().play(0, 16)

        self.bulletInUse[x] = False

    def hideExp( self, x ):
        self.exp[x].hide()





