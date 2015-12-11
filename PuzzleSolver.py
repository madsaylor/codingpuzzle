#coding utf-8

class PuzzleSolver:
    '''
    FindWords should return the number of all non-distinct occurrences 
    of the words found in the array, horizontally, vertically or diagonally, 
    and also the reverse in each direction. 
    The input to FindWords is a rectangular matrix of characters 
    (list of list of char).
    
    We are trying to see the quality of the code you write (hint: unit tests).  
    Don’t worry too much about performance and efficiency 
    but you program should work correctly. 
    It should also be capable of scaling to puzzles 
    with dimensions such as 4x4, 6x9, 9x9. 
    '''

    self.DICTIONARY = ['OX','CAT','TOY','AT','DOG','CATAPULT','T']
    self.input_list = None

    def IsWord(testWord):
        if testWord in self.DICTIONARY:
            return True
        return False

    def isValidInput():
        if not isinstance(self.input_list, list):
            return False
        else:
            inner_list_length = 0
            for char_list in self.input_list:
                if not isinstance(element, list):
                    return False
                else:
                    inner_list_length = len(element)

            for char_list in self.input_list:
                if len(element) != inner_list_length:
                    return False

            for char_list in self.input_list:
                for char in char_list:
                    if not isinstance(char, str) or char.isalpha() or \
                    len(char) != 1:
                        return False

            return True

    def findWords():
        '''
        X Z T A T Z
        C A O C A T
        Y O T H A Y
        X Z T A T Z
        I D N K S J
        G W E O P K
        '''
        self.input_list = input_list
        if self.isValidInput():
            for y, charList in enumerate(self.input_list):
                for x, char in enumerate(charList):
                    findWordsInCoords(x, y)

            
    def findWordsInCoords(x, y):
        pass
