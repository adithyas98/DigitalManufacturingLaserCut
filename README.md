# DigitalManufacturingLaserCut

![Constructed Acrylic Box](Resources/box.png)

Video: [https://www.youtube.com/watch?v=rqIyNnawNdU](https://www.youtube.com/watch?v=rqIyNnawNdU)

## How to Use It:

Change directories into the src folder and run main.py with the -h option to get instructions on how to use the script.

## How it Works:

There are four main components to the software:
- main
- Box
- SVG

These components will be described below

### SVG Class
This class implements all of the svg code. Here we have hardcoded svg code that accepts inputs to allow us to call these functions as necessary when making the box. Here is an example of the method that implements the rectangle svg object:

```python
    def rectangle(self,x,y,w,h,rx,ry):
        '''
        This will create a rectangle with the desired inputs
        Inputs:
            - x: starting x position
            - y: starting y position
            - w: width
            - h: height
            - rx: x radius for rounded corner
            - ry: y radius for rounded corner
        Output:
            - creates a rect object with the desired parameters
        '''
        rect = '<rect x="{}" y="{}" '.format(x,y)
        rect += 'width="{}" height="{}" '.format(w,h)
        rect += 'fill="{}" stroke-width="{}" '.format('none', 2)
        rect += ' stroke="{}" '.format('black')
        rect += ' rx="{}" ry="{}" />\n'.format(rx,ry)
        return rect
```
These methods allowed us to abstract away from the bare-bones svg code implementation and allowed us to focus more on the implementation of the box itself

### User Input Class
This class was created to allow for quick implementations of questions to ask the user prior to generating a box. This class also gives us the flexibility to ask any questions we want on the fly by simply making modifications to the dictionary that is sent in in the constructor. The primary method that is used to ask questions manually is the askQuestions which simply iterates through all of the keys in the dictionary (described above).The askQuestions method is shown below:


```python
    def askQuestions(self):
        '''
        This method will ask the questions defined in the qdata
        Output:
            - the qdata dictionary with a data label containing the data
            as follows:
                    Variable Code(code to access the answer)
                       (Create a sub dictionary)
                        - question: The Question to ask
                        - convert: pass in the conversion function
                                    pointer
                        - data: Contains the data
        '''
        #Print out the intro paragraph
        print("{}\n".format(self.intro))
        #iterate through the keys and ask the questions
        for key in self.qdict.keys():
            #find the conversion function
            convert = self.qdict[key]['convert']
            ans = input("{}\n".format(self.qdict[key]["question"]))#ask the question
            #Now we need to convert the data then add it to the dict
            try:
                self.fullDict[key]['data'] = convert(ans)
            except:
                print("Something was wrong in the input you provided\n")
                print("Please try again by restarting the script")
                return 1

        #once we have done this for everything, we can return fullData
        return self.fullDict
```
This class also allows the user to import their desired settings using a csv file that they can edit. A template csv file can be generated using the -o flag.

### Box Class

This class implements all of the sides of the box taking into account the measurements the user has inputted. These sides are then placed on the svg canvas such that the least amount of space is taken and no overlaps occur.



