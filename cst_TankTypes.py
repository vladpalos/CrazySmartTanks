#
#  Crazy Smart Tanks Game 2011

#
#   description:    Tank Types dictionaries (Tanks Configuration)
#   author:         Vlad Palos
#   date:           10.03.2011
#

        


from panda3d.core                           import *

## Collision Solids are only spheres for performance
## List of Point3 location coordonates and radius
## Two Collision Spheres for this model

TankType = []  

TankType.append(dict)

TankType [0] = {}
TankType [0] ['parts'] = 1
TankType [0] ['model'] = "data/models/Players/Tank1/tank.egg.pz"  
TankType [0] ['scale'] = 0.5  
TankType [0] ['weight'] = 30   # Tons 
TankType [0] ['rrange'] = 40    # Percent       

TankType [0] ['coll'] = []

TankType [0] ['coll'].append( Point3( -0.7 , 0.4,  1.7) )
TankType [0] ['coll'].append( 1.9 )

TankType [0] ['coll'].append( Point3( 2.9, 0.4, 1.7) )
TankType [0] ['coll'].append( 1.9 )

TankType [0] ['explosion_scale'] = 14
TankType [0] ['explosion_model'] = 'data/models/weapons/explosion2.egg'

TankType [0] ['explosion_sound'] = 'data/sounds/cb_shoot.mp3'
TankType [0] ['hit_sound'] = 'data/sounds/hit.wav'

TankType [0] ['ammo'] = {}

TankType [0] ['ammo'] ['load_bullets'] = 5

TankType [0] ['ammo'] ['model'] = "data/models/weapons/cannonball.egg"
TankType [0] ['ammo'] ['damage'] = 50 # How much life takes, form 1 to 100

TankType [0] ['ammo'] ['scale'] = 0.15
TankType [0] ['ammo'] ['texture'] = 'data/models/weapons/cannonball.jpg'

TankType [0] ['ammo'] ['explosion_scale'] = 6
TankType [0] ['ammo'] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

# Bullet starting position.Must be above tank to avoid starting collision
TankType [0] ['ammo'] ['bulletZ'] = 5 

TankType [0] ['ammo'] ['coll'] = []

TankType [0] ['ammo'] ['coll'].append( (0, 0, 0) )
TankType [0] ['ammo'] ['coll'].append( 2 )

TankType [0] ['ammo'] ['speed'] = 2.5
TankType [0] ['ammo'] ['ctime'] = 1 # Seconds

TankType [0] ['ammo'] ['sound_shoot'] = 'data/sounds/cb_shoot.mp3'
TankType [0] ['ammo'] ['sound_explode'] = 'data/sounds/cb_shoot.mp3'


#================================================================================
#================================================================================
#================================================================================
#================================================================================

TankType.append(dict)
TankType [1] = {}
TankType [1] ['parts'] = 1 
TankType [1] ['model'] = "data/models/Players/Tank2/tank1.egg.pz"  
TankType [1] ['scale'] = 0.5  
TankType [1] ['weight'] = 20   # Tons 
TankType [1] ['rrange'] = 40    # Percent       

TankType [1] ['coll'] = []

TankType [1] ['coll'].append( Point3( -1.4 , 0.4,  1.7) )
TankType [1] ['coll'].append( 1.9 )

TankType [1] ['coll'].append( Point3( 2.2, 0.4, 1.7) )
TankType [1] ['coll'].append( 1.9 )

TankType [1] ['explosion_scale'] = 10
TankType [1] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

TankType [1] ['explosion_sound'] = 'data/sounds/cb_shoot.mp3'
TankType [0] ['hit_sound'] = 'data/sounds/hit.wav'

TankType [1] ['ammo'] = {}

TankType [1] ['ammo'] ['load_bullets'] = 5

TankType [1] ['ammo'] ['model'] = "data/models/weapons/banana/banana.egg"
TankType [1] ['ammo'] ['damage'] = 10 # life, scale 1 to 100

TankType [1] ['ammo'] ['scale'] = 2
TankType [1] ['ammo'] ['texture'] = 'none'

TankType [1] ['ammo'] ['explosion_scale'] = 5
TankType [1] ['ammo'] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

# Bullet starting position.Must be above tank to avoid starting collision
TankType [1] ['ammo'] ['bulletZ'] = 4 

TankType [1] ['ammo'] ['coll'] = []

TankType [1] ['ammo'] ['coll'].append( (0, 0, 0) )
TankType [1] ['ammo'] ['coll'].append( 2 )

TankType [1] ['ammo'] ['speed'] = 2.5
TankType [1] ['ammo'] ['ctime'] = 0.3 # Seconds

TankType [1] ['ammo'] ['sound_shoot'] = 'data/sounds/bomb-01.wav'
TankType [1] ['ammo'] ['sound_explode'] = 'data/sounds/explode-01.wav'


#================================================================================
#================================================================================
#================================================================================
#================================================================================

TankType.append(dict)
TankType [2] = {}
TankType [2] ['parts'] = 1 
TankType [2] ['model'] = "data/models/Players/Tank2/tank1.egg.pz"  
TankType [2] ['scale'] = 0.5  
TankType [2] ['weight'] = 20   # Tons 
TankType [2] ['rrange'] = 40    # Percent       

TankType [2] ['coll'] = []

TankType [2] ['coll'].append( Point3( -1.4 , 0.4,  1.7) )
TankType [2] ['coll'].append( 1.9 )

TankType [2] ['coll'].append( Point3( 2.2, 0.4, 1.7) )
TankType [2] ['coll'].append( 1.9 )

TankType [2] ['explosion_scale'] = 10
TankType [2] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

TankType [2] ['explosion_sound'] = 'data/sounds/cb_shoot.mp3'

TankType [2] ['hit_sound'] = 'data/sounds/hit.wav'


TankType [2] ['ammo'] = {}

TankType [2] ['ammo'] ['load_bullets'] = 5

TankType [2] ['ammo'] ['model'] = "data/models/weapons/banana/banana.egg"
TankType [2] ['ammo'] ['damage'] = 10 # life, scale 1 to 100

TankType [2] ['ammo'] ['scale'] = 2
TankType [2] ['ammo'] ['texture'] = 'none'

TankType [2] ['ammo'] ['explosion_scale'] = 5
TankType [2] ['ammo'] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

# Bullet starting position.Must be above tank to avoid starting collision
TankType [2] ['ammo'] ['bulletZ'] = 4 

TankType [2] ['ammo'] ['coll'] = []

TankType [2] ['ammo'] ['coll'].append( (0, 0, 0) )
TankType [2] ['ammo'] ['coll'].append( 2 )

TankType [2] ['ammo'] ['speed'] = 2.5
TankType [2] ['ammo'] ['ctime'] = 0.3 # Seconds

TankType [2] ['ammo'] ['sound_shoot'] = 'data/sounds/bomb-01.wav'
TankType [2] ['ammo'] ['sound_explode'] = 'data/sounds/explode-01.wav'


#================================================================================
#================================================================================
#================================================================================
#================================================================================

TankType.append(dict)
TankType [3] = {}
TankType [3] ['parts'] = 1 
TankType [3] ['model'] = "data/models/Players/Tank2/tank1.egg.pz"  
TankType [3] ['scale'] = 0.5  
TankType [3] ['weight'] = 20   # Tons 
TankType [3] ['rrange'] = 40    # Percent       

TankType [3] ['coll'] = []

TankType [3] ['coll'].append( Point3( -1.4 , 0.4,  1.7) )
TankType [3] ['coll'].append( 1.9 )

TankType [3] ['coll'].append( Point3( 2.2, 0.4, 1.7) )
TankType [3] ['coll'].append( 1.9 )

TankType [3] ['explosion_scale'] = 10
TankType [3] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

TankType [3] ['explosion_sound'] = 'data/sounds/cb_shoot.mp3'

TankType [3] ['hit_sound'] = 'data/sounds/hit.wav'


TankType [3] ['ammo'] = {}

TankType [3] ['ammo'] ['load_bullets'] = 5

TankType [3] ['ammo'] ['model'] = "data/models/weapons/banana/banana.egg"
TankType [3] ['ammo'] ['damage'] = 10 # life, scale 1 to 100

TankType [3] ['ammo'] ['scale'] = 2
TankType [3] ['ammo'] ['texture'] = 'none'

TankType [3] ['ammo'] ['explosion_scale'] = 5
TankType [3] ['ammo'] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

# Bullet starting position.Must be above tank to avoid starting collision
TankType [3] ['ammo'] ['bulletZ'] = 4 

TankType [3] ['ammo'] ['coll'] = []

TankType [3] ['ammo'] ['coll'].append( (0, 0, 0) )
TankType [3] ['ammo'] ['coll'].append( 2 )

TankType [3] ['ammo'] ['speed'] = 2.5
TankType [3] ['ammo'] ['ctime'] = 0.3 # Seconds

TankType [3] ['ammo'] ['sound_shoot'] = 'data/sounds/bomb-01.wav'
TankType [3] ['ammo'] ['sound_explode'] = 'data/sounds/explode-01.wav'



#================================================================================
#================================================================================
#================================================================================
#================================================================================

TankType.append(dict)
TankType [4] = {}
TankType [4] ['parts'] = 1 
TankType [4] ['model'] = "data/models/Players/Tank2/tank1.egg.pz"  
TankType [4] ['scale'] = 0.5  
TankType [4] ['weight'] = 20   # Tons 
TankType [4] ['rrange'] = 40    # Percent       

TankType [4] ['coll'] = []

TankType [4] ['coll'].append( Point3( -1.4 , 0.4,  1.7) )
TankType [4] ['coll'].append( 1.9 )

TankType [4] ['coll'].append( Point3( 2.2, 0.4, 1.7) )
TankType [4] ['coll'].append( 1.9 )

TankType [4] ['explosion_scale'] = 10
TankType [4] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

TankType [4] ['explosion_sound'] = 'data/sounds/cb_shoot.mp3'

TankType [4] ['hit_sound'] = 'data/sounds/hit.wav'


TankType [4] ['ammo'] = {}

TankType [4] ['ammo'] ['load_bullets'] = 5

TankType [4] ['ammo'] ['model'] = "data/models/weapons/banana/banana.egg"
TankType [4] ['ammo'] ['damage'] = 10 # life, scale 1 to 100

TankType [4] ['ammo'] ['scale'] = 2
TankType [4] ['ammo'] ['texture'] = 'none'

TankType [4] ['ammo'] ['explosion_scale'] = 5
TankType [4] ['ammo'] ['explosion_model'] = 'data/models/weapons/explosion1.egg'

# Bullet starting position.Must be above tank to avoid starting collision
TankType [4] ['ammo'] ['bulletZ'] = 4 

TankType [4] ['ammo'] ['coll'] = []

TankType [4] ['ammo'] ['coll'].append( (0, 0, 0) )
TankType [4] ['ammo'] ['coll'].append( 2 )

TankType [4] ['ammo'] ['speed'] = 2.5
TankType [4] ['ammo'] ['ctime'] = 0.3 # Seconds

TankType [4] ['ammo'] ['sound_shoot'] = 'data/sounds/bomb-01.wav'
TankType [4] ['ammo'] ['sound_explode'] = 'data/sounds/explode-01.wav'


