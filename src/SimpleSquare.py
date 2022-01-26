#!/usr/bin/env python3

'''
This method will create a simple box with some text inside the box
'''

def square(w=10,h=10,text="Hello"):
    '''
    Inputs:
        - width: the width of the box (in cm)
        - height: the height of the box (in cm)
    Output:
        - outputs a svg file
    '''
    #Add the svg header info and define the viewport
    svg = '<svg viewBox="0 0 100cm 100cm" xmlns="http://www.w3.org/2000/svg">\n'
    #Add the square
    svg += '<rect x="10" y="10" width="{}cm" height="{}cm"  />\n'.format(str(w),str(h))
    #Add text
    svg += '<text x={}, y={},


