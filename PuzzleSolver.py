# coding=utf-8


class WrongInputException(ValueError):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return "Error code: {}. Message: {}".format(self.code, self.message)

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

    DICTIONARY = ['OX','CAT','TOY','AT','DOG','CATAPULT','T']
    input_list = None
    result = 0

    def __init__(self, input_list):
        self.input_list = input_list
        if self.isValidInput():
            return self    

    def IsWord(self, testWord):
        if testWord in self.DICTIONARY:
            return True
        return False

    def isValidInput(self):
        if not isinstance(self.input_list, list):
            raise WrongInputException(0, 'Init parameter is not instance of list')
        else:
            inner_list_length = 0
            for index, charList in enumerate(self.input_list):
                if not isinstance(charList, list):
                    raise WrongInputException(1, 'Row {} is not a list'.format(index))
                else:
                    inner_list_length = len(charList)

            for index, charList in enumerate(self.input_list):
                if len(charList) != inner_list_length:
                    raise WrongInputException(2, 'Row #{} have different length'.format(index))

            for i, charList in enumerate(self.input_list):
                for j, char in enumerate(charList):
                    if not isinstance(char, str):
                        raise WrongInputException(3, 'Element #{} in #{} is not string: "{}"'.format(j, i, char))
                    elif not char.isalpha():
                        raise WrongInputException(4, 'Element #{} in #{} row is not alphabetical: "{}"'.format(j, i, char))
                    elif len(char) != 1:
                        raise WrongInputException(5, 'Element #{} in #{} is not a single char: "{}"'.format(j, i, char))


    def findWords(self):        
        if self.isValidInput():
            for y, charList in enumerate(self.input_list):
                for x, char in enumerate(charList):
                    self.result += self.findWordsInCoords(x, y)
        return self.result

    def findWordsInCoords(self, x, y):
        axisList = self.getAxisListByCoords(x, y)
        for axis in axisList:
            for word in self.DICTIONARY:
                self.result += self.findWordInCharList(axis)

    def findWordInCharList(self, word, charList):
        result = 0        
        char_string = ''.join(charList)
        if len(word) == 1:
            result += char_string.count(word)
        else:
            result += sum(char_string[i:].startswith(word) for i in range(len(char_string)))
            result += sum(char_string[i:].startswith(word[::-1]) for i in range(len(char_string)))
                
        return result

    def getaAxis(self):
        axis = []
        map(lambda char_list: axis.append(char_list), self.input_list)
        
        diagonals = {
            'x_pos': self.input_list[y][x:],
            'x_neg': reversed(self.input_list[y][:x+1]),
            'y_pos': [charList[x] for charList in self.input_list[:y+1]],
            'y_neg': reversed([charList[x] for charList in self.input_list[y:]]),
            'diag_1_quad': [],
            'diag_2_quad': [],
            'diag_3_quad': [],
            'diag_4_quad': []
        }

        for v_index, charList in enumerate(reversed(charList[:y+1])):
            diagonals['diag_1_quad'].append(charList[x+v_index])

        for v_index, charList in enumerate(reversed(charList[:y+1])):
            if x-v_index >= 0:
                diagonals['diag_2_quad'].append(charList[x-v_index])

        for v_index, charList in enumerate(charList[:y+1]):
            if x-v_index >= 0:
                diagonals['diag_3_quad'].append(charList[x-v_index])

        for v_index, charList in enumerate(charList[y:]):
            diagonals['diag_4_quad'].append(charList[x+v_index])

        return list(diagonals.itervalues())