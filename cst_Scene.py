#
#  Crazy Smart Tanks Game 2011

#
#   description:    Environment/Scene Objects  
#   author:         Vlad Palos
#   date:           25.04.2011
#


from panda3d.core                               import *
import math
from direct.gui.OnscreenImage                   import OnscreenImage
from direct.filter.CommonFilters                import CommonFilters
import cst_FtTools
from direct.interval.IntervalGlobal             import * 

class cst_Scene :

    def __init__ (self, parent):

        
        ## Light settings   
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(0.5, 0.5, 0.5, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 0.4, 0, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))        

        ## Load Sky
        b = OnscreenImage(parent=render2dp, image="data/models/maps/space-green.jpg")
        base.cam2dp.node().getDisplayRegion(0).setSort(-20)

        ## Load fence model and duplicate it 
        fenceModel = loader.loadModel ("data/models/fence")
        fenceModel.setTransparency(TransparencyAttrib.MAlpha)
        fenceModel.setColor( 0.5, 0.1, 0.1 , 0.6)
        for i in range(8):
          placeholder = render.attachNewNode("fence-copy")
          placeholder.setPos(i*12.4-44, -parent.mapH, 0)
          fenceModel.instanceTo(placeholder)
          placeholder = render.attachNewNode("fence-copy")
          placeholder.setPos(i*12.4-44, parent.mapH, 0)
          fenceModel.instanceTo(placeholder)
          placeholder = render.attachNewNode("fence-copy")
          placeholder.setH(90)
          placeholder.setPos(parent.mapW, i*12.4-44, 0)
          fenceModel.instanceTo(placeholder)
          placeholder = render.attachNewNode("fence-copy")
          placeholder.setH(90)
          placeholder.setPos(-parent.mapW, i*12.4-44, 0)
          fenceModel.instanceTo(placeholder)

        ## Load Other Objects
                
        lamp1 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp1.reparentTo(render)        
        lamp1.setScale (0.6)
        lamp1.setPos (39, 49, 0)
        lamp1.lookAt(0, 0, 0)

        lamp2 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp2.reparentTo(render)        
        lamp2.setScale (0.6)
        lamp2.setPos (-39, 49, 0)
        lamp2.lookAt(0, 0, 0)

        lamp3 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp3.reparentTo(render)        
        lamp3.setScale (0.6)
        lamp3.setPos (-39, -49, 0)
        lamp3.lookAt(0, 0, 0)

        lamp4 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp4.reparentTo(render)        
        lamp4.setScale (0.6)
        lamp4.setPos (39, -49, 0)
        lamp4.lookAt(0, 0, 0)

        lamp5 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp5.reparentTo(render)        
        lamp5.setScale (0.6)
        lamp5.setPos (-14, -49, 0)
        lamp5.lookAt(0, 0, 0)

        lamp6 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp6.reparentTo(render)        
        lamp6.setScale (0.6)
        lamp6.setPos (14, -49, 0)
        lamp6.lookAt(0, 0, 0)

        lamp7 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp7.reparentTo(render)        
        lamp7.setScale (0.6)
        lamp7.setPos (-14, 49, 0)
        lamp7.lookAt(0, 0, 0)

        lamp8 = loader.loadModel ("data/models/lamp1/lamp.egg")
        lamp8.reparentTo(render)        
        lamp8.setScale (0.6)
        lamp8.setPos (14, 49, 0)
        lamp8.lookAt(0, 0, 0)
                
        b1 = loader.loadModel('data/models/building1/BuildingCluster1.egg')
        b1.reparentTo(render)        
        b1.setScale (0.2)
        b1.setPos(-60,30,0)        
        b1.lookAt(0, 30, 0)
        
        b2 = loader.loadModel('data/models/building2/BuildingCluster2.egg')
        b2.reparentTo(render)        
        b2.setScale (0.3)
        b2.setPos(54,56,0)        
        b2.lookAt(0, 56, 0)

        b3 = loader.loadModel('data/models/building3/BuildingCluster3.egg')
        b3.reparentTo(render)        
        b3.setScale (0.17)
        b3.setPos(-55, 63,0)        
        b3.lookAt(0, 0, 0)

        b4 = loader.loadModel('data/models/building4/BuildingCluster4.egg')
        b4.reparentTo(render)        
        b4.setScale (0.16)
        b4.setPos(60, -50,0)        
        b4.lookAt(0, 0, 0)

        b5 = loader.loadModel('data/models/building4/BuildingCluster4.egg')
        b5.reparentTo(render)        
        b5.setScale (0.19)
        b5.setPos(-60, -50,0)        
        b5.lookAt(0, 0, 0)

        b6 = loader.loadModel('data/models/building6/Museum.egg')
        b6.reparentTo(render)        
        b6.setScale (0.2)
        b6.setPos(-60, -10,0)        
        b6.lookAt(0, -10, 0)

        b7 = loader.loadModel('data/models/building5/BuildingCluster5.egg')
        b7.reparentTo(render)        
        b7.setScale (0.19)
        b7.setPos(57, 20,0)        
        b7.lookAt(0, 20, 0)

        b8 = loader.loadModel('data/models/building6/Museum.egg')
        b8.reparentTo(render)        
        b8.setScale (0.2)
        b8.setPos(57, -30,0)        
        b8.lookAt(0, -30, 0)


        b4 = loader.loadModel('data/models/CityHall/CityHall.egg')
        b4.reparentTo(render)        
        b4.setScale (0.3)
        b4.setPos(0, 63,0)        
        b4.lookAt(0, 0, 0)

####  + Collissions

        statue = loader.loadModel('data/models/statue/Statue.egg')
        statue.reparentTo(render)        
        statue.setScale (1.3)
        statue.setPos(0, 0,0)        
        statue.lookAt(0, -100, 0)
        statue.setColor(0.3, 0.4,0.1)

        statueCollNode = render.attachNewNode( CollisionNode( "statue" ) )

#        statueCollNode.node().addSolid( CollisionSphere( (0, 0, 0), 1 ) )        

#        parent.pusher.addCollider( statueCollNode, statue )
        base.cTrav.addCollider( statueCollNode, parent.pusher )


####  + Plane Movement
    
        plane = loader.loadModel('data/models/plane2/blimp.egg')
        plane.reparentTo(render)
        plane.setPos(-1000, 0, 0)
        plane.lookAt(500, 0, 0)
        plane.setScale (0.1)
 
####  + Cow
    
        cow = loader.loadModel ('data/models/Cow/Cow.egg')
        cow.reparentTo (render)
        cow.setPos(55, -44, 0)
        cow.lookAt (0, -45, 0)
        cow.setScale (0.6)
        cowSound = loader.loadSfx('data/sounds/cow.wav')

####   + Cinem

        self.cinem = Sequence (
                    Parallel (
                        Sequence(plane.posInterval(40,(400, 45, 10), startPos= (-100, 45, 10))),
                        SoundInterval (cowSound,loop = 0)            
                    ),
                    Func (self.addCinemTask)
                )
        self.addCinemTask()

    def addCinemTask(self):
        taskMgr.doMethodLater(5, self.doCinem, 'Cinematics')       

    def doCinem(self,task):
        self.cinem.start()
        
        return task.done    
        
