#!/usr/bin/env python3

'''
This method will create a simple box with some text inside the box
'''

def square(w=10,h=10,text='AS and SA'):
    '''
    Inputs:
        - width: the width of the box (in cm)
        - height: the height of the box (in cm)
        - length: the length of the box (in cm)
        - thickness: thickness of material (in cm)
    Output:
        - outputs a svg file
    '''
    #Add the svg header info and define the viewport
    svg = '<svg viewBox="0 0 100cm 100cm" xmlns="http://www.w3.org/2000/svg">\n'
    #Add the square
    svg += '<rect x="0.1cm" y="0.1cm" width="{}cm" height="{}cm" style="stroke: #009900; stroke-width: 3; fill:none;"/>\n'.format(str(w),str(h))
    #Add text
    svg += '<text x="{}cm" y="{}cm" dominant-baseline="middle" text-anchor="middle" font-size="1cm">{}</text>\n'.format(str(0.1+w/2),str(0.1+h/2),text)
    #End the svg file
    svg += '</svg>'
    #return the output
    return svg
    
    
if __name__ == "__main__":
    with open("square.svg","w") as f:
        f.write(square(w=5.08,h=5.08))
        
