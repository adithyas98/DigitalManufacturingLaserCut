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
        alpha_w: default width of screw T-holes
        alpha_l: default length of screw T-holes
        r: radius of screw hole
        sqnut_w: square nut width
        sqnut_t: square nut thickness
        originX: this is where x-position of the box will start
        originY: this is where y-position of the box will start
    '''


    def __init__(self):
        self.SVGcode=[]
        self.debug = True #Simple debug variable
             
    def Base(self):
        #function to cut out the base of the box
        originx = originX #sets the x point where the base starts
        originy = originY #sets the y point where the base starts
                
        #main rectangle
        base=SVG.rectangle(origin,origin, w, l, beta, beta)
        
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
        
    def FrontBack(self, offestX, offsetY):
        #function to cut out the front and back  panels of the box
         
        originx = originX + offsetX #sets the x point where the panel starts
        originy = originY + offsetY #sets the y point where the panel starts
        
        #outside perimeter
        base=SVG.rectangle(originx,originy, l, h-2*t, beta, beta)
        
        #screw T-hole 1 vertical
        base+=SVG.rectangle(originx+0.2*l-0.5*alpha_w, originy+h-2*t-alpha_l, alpha_w, alpha_l, 0, 0)
        
        #screw T-hole 1 square nut
        base+=SVG.rectangle(originx+0.2*l-0.5*alpha_w, originy+h-2*t-0.5*alpha_l, sqnut_w, sqnut_t, 0, 0)
        
        #screw T-hole 2 vertical
        base+=SVG.rectangle(originx+0.4*l-0.5*alpha_w, originy+h-2*t-alpha_l, alpha_w, alpha_l, 0, 0)
        
        #screw T-hole 2 square nut
        base+=SVG.rectangle(originx+0.4*l-0.5*alpha_w, originy+h-2*t-0.5*alpha_l, sqnut_w, sqnut_t, 0, 0)
        
        #mating slit 1
        base+=SVG.rectangle(originx+beta, originy, t+0.05*t, 0.5*(h-2*t), 0, 0)
        
        #mating slit 2
        base+=SVG.rectangle(originx+l-beta-(t+0.05*t), originy, t+0.05*t, 0.5*(h-2*t), 0, 0)
        
        
        
        
        
        


