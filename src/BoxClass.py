<<<<<<< Updated upstream
#!/usr/bin/env python3

from SVGclass import SVG
from UIClass import UserInput

class Box:
    '''
    This class will implement the Box and relies on the SVG and the 
    UI classes to draw lines and receive measurements respectively.
    
    The following class variables are obtained from UIClass:
        l: total length of the box
        w: total width of the box
        t: thickness of the material
        
    The following class variables are preset:
        beta: default offset of inserts and radius of rounded edges
        alpha: default width of inserts
        r: radius of screw hole
    '''


    def __init__(self):
        self.SVGcode=[]
        self.debug = True #Simple debug variable
             
    def base(self):
        
        origin = 10 #sets the point where the base starts
                
        #main rectangle
        base+=SVG.rectangle(origin,origin, w, l, beta, beta)
        
        #top left screw hole 1
        base+=SVG.circle(origin+0.2*l, origin+beta, r)
        
        #top right screw hole 1
        base+=SVG.circle(origin+0.8*l, origin+beta, r)
        
        #bottom left screw hole 1
        base+=SVG.circle(origin+0.2*l, origin+w-beta, r)
        
        #bottom right screw hole 1
        base+=SVG.circle(origin+0.8*l, origin+w-beta, r)
        
        #top left screw hole 2
        base+=SVG.circle(origin+beta, origin+0.2*w, r)
        
        #top right screw hole 2
        base+=SVG.circle(origin+l-beta, origin+0.2*w, r)
        
        #bottom left screw hole 2
        base+=SVG.circle(origin+beta, origin+0.8*w, r)
        
        #bottom right screw hole 2
        base+=SVG.circle(origin+l-beta, origin+0.8*w, r)
        
        self.SVGcode.append(base)
        


