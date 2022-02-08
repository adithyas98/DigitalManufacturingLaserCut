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
        self.SVGcode=[]#blank list to hold 
        self.debug = True #Simple debug variable
        self.SVG = SVG()
        #create the question dictionary
        intro = "Please answer the following questions. All measurements are in cm"
        qdict = dict()
        #Find the length
        qdict['l']['question'] = "What length do you want for the box?"
        qdict['l']['convert'] = float
        #Find the height
        qdict['h']['question'] = "What height do you want for the box?"
        qdict['h']['convert'] = float

        #Find the width
        qdict['w']['question'] = "What width do you want for the box?"
        qdict['w']['convert'] = float

        #Find the thickness of material
        qdict['t']['question'] = "What is the thickness of the material?"
        qdict['t']['convert'] = float

        #Find the dpi 
        qdict['dpi']['question'] = "What is your Screen's dpi?\n Find it using this link :https://www.infobyip.com/detectmonitordpi.php"
        qdict['dpi']['convert'] = int

        #Create a UI class and ask questions
        ui = UserInput(qdict,intro)
        #Now we can ask the questions
        self.qdata = ui.askQuestions()


    def top(self,originX=80,originY):
        '''
        This method will create the top of the box
        Inputs:
            - originX: Where the top of the box will start on the canvas
                    (x-axis)
            - originY: Where the top of the box will start on the canvas
                    (y-axis)
        Output:
            - None: will just append component to self.SVGCode
        '''
        #define our parameters
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        beta = 1.50 * t

        #TODO: NEED TO DEFINE ALPHA!!!
        alpha = 0.1
        #TODO: NEED TO DEFINE r!!!
        r = 0.01 

        #First we need to create overall rect
        top = ''
        top += self.SVG.rectangle(originX,originY,w,h,r,r)
        #Now we need to code in the cut out rectangles

        #left hand side
        #find cutout height and width
        ch = beta - 0.5*(t-0.05*t)
        cw = t + 0.05*t
        top += self.SVG.rectangle(originX,originY,cw,ch,rx=0,ry=0)

        #find the origin for the next cutout on the left side
        botCutOriginY = originY + ch + t - 0.05*t
        #now we can cut the same rectangle out
        top += self.SVG.rectangle(originX,botCutOriginY,cw,ch,rx=0,ry=0)


        #Code the cutouts on the right hand side
        #Find the new x origin
        rightOriginX = originX + (w - (t + 0.05*t))
        
        #We can pretty much use the same measurements as before
        top += self.SVG.recangle(rightOriginX,originY,cw,ch,rx=0,ry=0)

        #Now we just need to shift the start of the bottom cutout rect
            #by the same amount we did before
        top += self.SVG.rectangle(rightOriginX,botCutOriginY,cw,ch,rx=0,ry=0)

        #Now we can append our top to array
        self.SVGCode.append(top)
             
    def base(self,origin=10):
        '''
        This method will create the bottom of the box.
        Inputs:
            - origin:The origin of the bottom
        ouput:
            - None, simply appends to self.SVGCode
        '''
        #define our parameters
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        beta = 1.50 * t

        #TODO: NEED TO DEFINE ALPHA!!!
        alpha = 0.1
        #TODO: NEED TO DEFINE r!!!
        r = 0.01 
        #TODO: Try to have an origin x and and origin y variable
                #for more flexibility

        
        #main rectangle
        base+=self.SVG.rectangle(origin,origin, w, l, beta, beta)
        
        #top left screw hole 1
        base+=self.SVG.circle(origin+0.2*l, origin+beta, r)
        
        #top right screw hole 1
        base+=self.SVG.circle(origin+0.8*l, origin+beta, r)
        
        #bottom left screw hole 1
        base+=self.SVG.circle(origin+0.2*l, origin+w-beta, r)

        #bottom right screw hole 1
        base+=self.SVG.circle(origin+0.8*l, origin+w-beta, r)
        
        #top left screw hole 2
        base+=self.SVG.circle(origin+beta, origin+0.2*w, r)
        
        #top right screw hole 2
        base+=self.SVG.circle(origin+l-beta, origin+0.2*w, r)
        
        #bottom left screw hole 2
        base+=self.SVG.circle(origin+beta, origin+0.8*w, r)
        
        #bottom right screw hole 2
        base+=self.SVG.circle(origin+l-beta, origin+0.8*w, r)
        
        self.SVGcode.append(base)
    def LeftRight(self,originX,originY):
        '''
        This method will implement the left and right sides of the box
        which includes the hinge mechanism
        '''
        #TODO: Complete this method
        pass
    def exportBox(self,fileName):
        '''
        Will run all the methods and export the box 
        Inputs:
            - fileName: Desired name of the outputed svg file
        Output:
            - Nothing is returned, but the svg file is created and saved
        '''
        #we want to run the methods first:


        #Now we can open a file and add the contents of our list
        with open(fileName) as f:
            for element in self.SVGCode:
                f.write(element)
                f.write('\n')#add a new line item
        
    def convertPxtoCm(self,px):
        '''
        This method will convert to cm from pixels
        Input:
            - px: Pixel value to convert to cm
        Output:
            - cm measurement for the input
        '''
        dpi = qdata['dpi']['data'] #retrieve the dpi of the monitor
        return (2.54/dpi)*px
        
    def convertCmtoPx(self,cm):
        '''
        This method will convert to pixels from cm
        Input:
            - cm: cm measurement
        Output:
            - The px measurment for the input
        '''
        dpi = qdata['dpi']['data']
        return (dpi/2.54) * cm


if __name__ == '__main__':
    #create a simple box class and test out the methods
