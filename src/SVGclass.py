#!/usr/bin/env python3



class SVG:
    '''
    This class will implement all necessary SVG code
    Attributes:
       strokeWidth: The default width of the stroke that will be output in the svg file
    Methods:
        
    '''
    def __init__(self,strokeWidth=3):
        self.strokeWidth = 3 #The stroke width
        self.debug = True #Simple debug variable

    def header(self):
        '''
        Will write the header file to start an svg script
        '''
        
        header = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n'

        return header

    def footer(self):
        '''

        Will write the footer to close the svg script
        '''
        return '\n</svg>\n'

    def polyline(self,points,stroke='black',fill="none"):
        '''
        This will create a poly line based on the points given
        Inputs:
            - points: An array of tuples containing x and y coordinates
                    [(x1,y1),(x2,y2),...]
        output:
            - polyline svg code
        '''
        #We need to generate the string of coordinates
        cords = ""
        for i,c in enumerate(points):
            if i == len(points):
                #Then we dont want to have a space
                cords += "{},{}".format(str(c[0]),str(c[1]))
            else:
                cords += "{},{} ".format(str(c[0]),str(c[1]))

        if self.debug:
            print("The coordinates going into Polyline:{}".format(cords))
        polyline = '<polyline points="{}" '.format(cords)

        polyline+= 'fill="{}" stroke="{}" '.format(fill,stroke)

        polyline += 'stroke-width="{}"/>'.format(self.strokeWidth)

        return polyline


if __name__ == '__main__':
    svg = SVG()
    points = [(10,1),(10,30)]
    poly = svg.polyline(points)

    header = svg.header()
    footer = svg.footer()

    with open('test.svg','w') as f:
        f.write(header)
        f.write(poly)
        f.write(footer)

