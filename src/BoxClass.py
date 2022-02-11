#!/usr/bin/env python3

from SVGclass import SVG
from UIClass import UserInput
from collections import defaultdict
import os

class Box:
    '''
    This class will implement the Box and relies on the SVG and the 
    UI classes to draw lines and receive measurements respectively.
    
    The following class variables are obtained from UIClass:
        l: total length of the box
        w: total width of the box
        h: height of the box
        t: thickness of the material
    
    The following class variables are preset:
        beta: default offset of inserts and radius of rounded edges
        alpha_w: default width of screw T-holes
        alpha_l: default length of screw T-holes
        r: radius of screw hole
        sqnut_w: square nut width
        sqnut_t: square nut thickness
    '''

    def __init__(self,fileInput=None,questionOut=False):
        self.SVGcode=[]#blank list to hold 
        self.debug = False #Simple debug variable
        self.SVG = SVG()
        #create the question dictionary
        intro = "Please answer the following questions. All measurements are in cm"
        qdict = defaultdict(dict)
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
        
        #Ask user if they want text on the front of the box 
        qdict['engraving']['question'] = "Type the text you want to engrave on the front face of the box. Type NA if you do not want any engraving. "
        qdict['engraving']['convert'] = str

        #Ask user if they want Columbia Logo on the front face of the box
        qdict['Logo']['question'] = "Do you want to engrave the Columbia logo on the front face of the box? Type YES or NO: "
        qdict['Logo']['convert'] = str
        
        #Create a UI class and ask questions
        ui = UserInput(qdict,intro)
        #Now we can ask the questions
        if fileInput is not None and not questionOut:
            #Then we want to input the file the user has given us
            self.qdata = ui.inputCSV(fileInput)
        elif questionOut:
            #Then we want to run the output file method
            print(ui.outputQuestions("{}.csv".format(fileInput)))
            quit()
        else:
            self.qdata = ui.askQuestions()

        if self.qdata == 1:
            #Then there was some error and we should just stop the script here
            print("Exiting")
            quit()
        elif not self.checkDims():
            #Then we have an issue with the dimensions
            print("There was an error with your dimensions, please try again.")
            print("Exiting program, please restart and try again.")
            quit()
        '''
        TODO:We don't actually need to do this since we have the dictionary
        #retrieve values for global variables
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        beta = 1.25*t
        '''

        #TODO: Need to set the following variables
        #alpha,beta, and screw and nut parameters

        


    def top(self,originX,originY):
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
        beta = 1.25*t

        #First we need to create overall rect
        top = ''
        top += self.SVG.rectangle(originX,originY,l,w,0,0)
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
        rightOriginX = originX + (l - (t + 0.05*t))
        
        #We can pretty much use the same measurements as before
        top += self.SVG.rectangle(rightOriginX,originY,cw,ch,rx=0,ry=0)

        #Now we just need to shift the start of the bottom cutout rect
            #by the same amount we did before
        top += self.SVG.rectangle(rightOriginX,botCutOriginY,cw,ch,rx=0,ry=0)

        #Now we can append our top to array
        self.SVGcode.append(top)
             
    def base(self,originX, originY):
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
        beta = 1.25*t

        #screw head radius
        r = self.convertCmtoPx(0.212)

        base =''
        #main rectangle
        base+=self.SVG.rectangle(originX,originY, l, w, beta, beta)

        
        #top left screw hole 1
        base+=self.SVG.circle(originX+0.2*l, originY+beta, r)
        
        #top right screw hole 1
        base+=self.SVG.circle(originX+0.8*l, originY+beta, r)
        
        #bottom left screw hole 1
        base+=self.SVG.circle(originX+0.2*l, originY+w-beta, r)

        #bottom right screw hole 1
        base+=self.SVG.circle(originX+0.8*l, originY+w-beta, r)
        
        #top left screw hole 2
        base+=self.SVG.circle(originX+beta, originY+0.2*w, r)
        
        #top right screw hole 2
        base+=self.SVG.circle(originX+l-beta, originY+0.2*w, r)
        
        #bottom left screw hole 2
        base+=self.SVG.circle(originX+beta, originY+0.8*w, r)
        
        #bottom right screw hole 2
        base+=self.SVG.circle(originX+l-beta, originY+0.8*w, r)
        
        self.SVGcode.append(base)
        

    def logo(self, filename):
        #this method reads in the Columbia Logo file in text form
        with open(filename, 'r') as f:
            logocode = f.read()
        f.close()    
        return logocode    
    
    def front(self, originx, originy):
        #function to cut out the front and back  panels of the box
        
        #define our paramters
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        beta = 1.25*t
        
        #screw and nut dimensions
        #TODO: Make these into variables we can modify incase we are wrong
        sqnut_w = self.convertCmtoPx(0.48)
        sqnut_t = self.convertCmtoPx(0.16)
        alpha_w = self.convertCmtoPx(0.22)
        alpha_l = self.convertCmtoPx(0.96)        
        
        #effective height of the front panel
        y= h-2*t
        
        front =''
        #outside perimeter
        front+=self.SVG.rectangle(originx, originy, l, y, beta, beta)
        
        
        #screw T-hole 1 vertical
        front+=self.SVG.rectangle(originx+0.2*l-0.5*alpha_w, originy+h-2*t-alpha_l, alpha_w, alpha_l, 0, 0)
        
        #screw T-hole 1 square nut
        front+=self.SVG.rectangle(originx+0.2*l-0.5*sqnut_w, originy+h-2*t-0.5*alpha_l, sqnut_w, sqnut_t, 0, 0)
        
        #screw T-hole 2 vertical
        front+=self.SVG.rectangle(originx+0.8*l-0.5*alpha_w, originy+h-2*t-alpha_l, alpha_w, alpha_l, 0, 0)
        
        #screw T-hole 2 square nut
        front+=self.SVG.rectangle(originx+0.8*l-0.5*sqnut_w, originy+h-2*t-0.5*alpha_l, sqnut_w, sqnut_t, 0, 0)
        
        #mating slit 1
        front+=self.SVG.rectangle(originx+beta, originy, t+0.05*t, 0.5*(h-2*t), 0, 0)
        
        #mating slit 2
        front+=self.SVG.rectangle(originx+l-beta-(t+0.05*t), originy, t+0.05*t, 0.5*(h-2*t), 0, 0)
        
        #Columbia Logo
        if self.qdata['Logo']['data'] == 'YES':
            front+=self.logo('ColumbiaLogoTextFile.txt').format(originx-350, originy-250)
        
        self.SVGcode.append(front)
        
    def back(self, originx, originy):
        #function to cut out the front and back  panels of the box
        
        #define our paramters
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        beta = 1.25*t
        
        #screw and nut dimensions
        sqnut_w = self.convertCmtoPx(0.48)
        sqnut_t = self.convertCmtoPx(0.16)
        alpha_w = self.convertCmtoPx(0.22)
        alpha_l = self.convertCmtoPx(0.96)        
        
        #effective height of the front panel
        y= h-2*t
        
        back =''
        #outside perimeter
        back+=self.SVG.rectangle(originx, originy, l, y, beta, beta)
        
        
        #screw T-hole 1 vertical
        back+=self.SVG.rectangle(originx+0.2*l-0.5*alpha_w, originy+h-2*t-alpha_l, alpha_w, alpha_l, 0, 0)
        
        #screw T-hole 1 square nut
        back+=self.SVG.rectangle(originx+0.2*l-0.5*sqnut_w, originy+h-2*t-0.5*alpha_l, sqnut_w, sqnut_t, 0, 0)
        
        #screw T-hole 2 vertical
        back+=self.SVG.rectangle(originx+0.8*l-0.5*alpha_w, originy+h-2*t-alpha_l, alpha_w, alpha_l, 0, 0)
        
        #screw T-hole 2 square nut
        back+=self.SVG.rectangle(originx+0.8*l-0.5*sqnut_w, originy+h-2*t-0.5*alpha_l, sqnut_w, sqnut_t, 0, 0)
        
        #mating slit 1
        back+=self.SVG.rectangle(originx+beta, originy, t+0.05*t, 0.5*(h-2*t), 0, 0)
        
        #mating slit 2
        back+=self.SVG.rectangle(originx+l-beta-(t+0.05*t), originy, t+0.05*t, 0.5*(h-2*t), 0, 0)
        
        self.SVGcode.append(back)
        
    def side(self,originX,originY):
        '''
        This method will implement the left and right sides of the box
        which includes the hinge mechanism
        '''
        #define our parameters
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        beta = 1.25*t
        alpha = self.alpha
        side = ''

        #Create the first rectangle 
        #We need to recalculate the height of the box 
                #since we will be cutting a lot of stuff out
        sideHeight = (h-2*t) + 2*beta + t
        
        #Inputs for SVG Rectangle: rectangle(self,x,y,w,h,rx,ry):
        #Now make the big rectangle
        side += self.SVG.rectangle(originX,originY,w,sideHeight,0,0)
        #Now draw the smaller rectangles to cut out the parts
        
        #Cut out the hinge square
        hingeX = originX + 2*beta #calculate the new x coordinate

        side += self.SVG.rectangle(hingeX,originY,w-2*beta,2*beta,0,0)
        #now cut a whole
        #Inputs for svg Circle: circle(self,x,y,r):
            #x,y are for center of circle
        side += self.SVG.circle(originX+beta,originY+beta,t/2)


        #Now, we can cut out the slits
        #First do the left one
        leftSlitX = originX + beta
        slitY = originY + 0.5*(h-2*t)

        slitHeight = 0.5*(h-2*t)

        #Make the right slit

        side += self.SVG.rectangle(leftSlitX,slitY,t,slitHeight)


        #Now, make the right slit
        rightSlitX = originX + (w - t - beta)

        side += self.SVG.rectangle(rightSlitX,slitY,t,slitHeight)


        #Now cut out the inserts
        #Find the y coordinate starting point for all cut outs
        insertY =  2*beta + (h-2*t)
        phi = alpha - alpha*0.05 #The length of the insert
        #Inputs for SVG Rectangle: rectangle(self,x,y,w,h,rx,ry):

        #Section 1: Before first insert
        sec1Width = 0.2*w - phi

        #Cut the rectangle
        side += self.SVG.rectangle(originX,insertY,sec1Width,t,0,0)

        #Section 2: In between inserts
        sec2Width = w - (0.2*w+0.5*phi) - (0.5*phi+0.2*w)
        sec2X = 0.2*w+0.5*phi

        side += self.SVG.rectangle(sec2X,insertY,sec2Width,t,0,0)


        #Section 3: Cutout after the second insert
        sec3X = w - 0.2*w + 0.5*phi
        sec3Width = originX + w - 0.2*w + 0.5*phi

        side += self.SVG.rectangle(sec3X,insertY,sec3Width,t,0,0)

        self.SVGcode.append(side)


       
    def exportBox(self,fileName):
        '''
        Will run all the methods and export the box 
        Inputs:
            - fileName: Desired name of the outputed svg file
        Output:
            - Nothing is returned, but the svg file is created and saved
        '''
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        
        #we want to run the methods first:
        self.top(10,10)
        self.base(10+t+l,10)
        self.back(10,10+w+t)
        self.front(10+t+l,10+w+t)
        

        #Now we can open a file and add the contents of our list
        with open(fileName,'w') as f:
            f.write(self.SVG.header())
            for element in self.SVGcode:
                f.write(element)
                f.write('\n')#add a new line item
            f.write(self.SVG.footer())
        
    def convertPxtoCm(self,px):
        '''
        This method will convert to cm from pixels
        Input:
            - px: Pixel value to convert to cm
        Output:
            - cm measurement for the input
        '''
        dpi = self.qdata['dpi']['data'] #retrieve the dpi of the monitor
        return (2.54/dpi)*px
        
    def checkDims(self):
        '''
        Checks the dimensions to see if there are any issues
        Inputs:
            - None
        Outputs:
            - return True if dims are good
            - return False if dims are bad
        '''
        l = self.convertCmtoPx(self.qdata['l']['data'])
        w = self.convertCmtoPx(self.qdata['w']['data'])
        h = self.convertCmtoPx(self.qdata['h']['data'])
        t = self.convertCmtoPx(self.qdata['t']['data'])
        if l<9 or l>15:
            return False
        if w<9 or w>15:
            return False
        if h<9 or h>15:
            return False
        if t>1:
            return False
        #If we meet all of these checks, then return true
        return True

        
    def convertCmtoPx(self,cm):
        '''
        This method will convert to pixels from cm
        Input:
            - cm: cm measurement
        Output:
            - The px measurment for the input
        '''
        dpi = self.qdata['dpi']['data']
        return (dpi/2.54) * cm


if __name__ == '__main__':
    #create a simple box class and test out the methods
    box = Box()
    box.exportBox("/Output/TestBox.svg")#All the functions we wrote will be run here

