#
#  Crazy Smart Tanks Game 2011

#
#   description:    CST - Tools (Functions)
#   author:         Vlad Palos
#   date:           15.03.2011
#

        
from pandac.PandaModules                import Point2, Point3

def map3dToAspect2d(node, point):

    # Convert the point to the 3-d space of the camera
    p3 = base.cam.getRelativePoint(node, point)

    # Convert it through the lens to render2d coordinates
    p2 = Point2()

    if not base.camLens.project(p3, p2):
        return None

    r2d = Point3(p2[0], 0, p2[1])

    # And then convert it to aspect2d coordinates
    a2d = aspect2d.getRelativePoint(render2d, r2d)

    return a2d 

def distSq(p0, p1):
    return (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2

