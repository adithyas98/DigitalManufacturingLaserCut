#!/usr/bin/env python3

import sys
from BoxClass import Box

def main():
    '''
    Main method that will run all of our code
    '''
    #Parse arguments
    #global box
    if len(sys.argv) == 1:
        print("Box class will be run normally")
        box = Box()
    elif sys.argv[1] == '-h':
        print("You have three options for flags:\n")
        print("-o {FileName.csv} will create an editable csv file with ")
        print("the inputs needed to make your box. You can add your specifications in the ")
        print("Input column of the csv\n")
        print("-i {FileName.csv} will import your specifications from the file specified\n")
        print("Run the file with no arguments to have the script manually ask you for each input")
    elif sys.argv[1] == '-o':
        box = Box(fileInput=sys.argv[2],questionOut=True)
    elif sys.argv[1] == '-i':
        print("Data will be imported from the file")
        box = Box(fileInput=sys.argv[2],questionOut=False)
    else:
        print("Unrecognized input")
        print("Try -h for help")
        quit()
    #Generate the box now
    filename = input("What you like to name the file? Just give us the name, we will handle the rest!")
    box.exportBox("{}.svg".format(filename))
    








if __name__ == '__main__':
    main()