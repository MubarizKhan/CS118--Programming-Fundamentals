#Fill in the Line class methods to accept coordinates as a pair of tuples 
# and return the slope and distance of the line.
import math


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        dist = (((x2-x1) ** 2) - ((y2 -y1) **2)) ** 0.5
        print (dist)
        return dist
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        print ((y2-y1) / (x2 - x1))
        return (y2-y1) / (x2 - x1)


cob = (9,2)
nob = (4,4)

line = Line(cob,nob)

line.distance()
line.slope()


#Problem 2



class Cylinder:
    

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        pi = 3.142

        vol = (pi * (self.radius ** 2) * self.height)
        print (vol)
        return vol
    
    def surface_area(self):
        pi = 3.142

        sa = (2 * pi * self.radius * self.height) + (2 * pi * (self.radius ** 2))
        print (sa, "<----Surface area ")
        return sa


cox = Cylinder(12,3) 
cox.volume()
cox.surface_area()

