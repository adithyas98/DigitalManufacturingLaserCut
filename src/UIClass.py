#!/usr/bin/env python3


class UserInput:
    '''
    Class will define methods to accept user input
    '''
    def __init__(self,qdict,intro):
        '''
        Input:
            - dictionary: A dictionary of inputs to ask the user
                - The dictionary should take the following form
                    Variable Code(code to access the answer)
                       (Create a sub dictionary)
                        - question: The Question to ask
                        - convert: pass in the conversion function
                                    pointer
            - intro: What you would like to start the questioning with
        '''
        self.intro = intro
        self.qdict = qdict
        self.fullDict = qdict  #Used once we have our answers

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
            ans = input(self.qdict[key]["question"])#ask the question
            #Now we need to convert the data then add it to the dict
            self.fullDict[key]['data'] = convert(ans)

        #once we have done this for everything, we can return fullData
        return self.fullDict

    ##TODO: Create a method to output a text file of questions
    ##TODO: Create a method to input answers from the text file






        

        

        
