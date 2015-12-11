# coding=utf-8

import unittest
from PuzzleSolver import PuzzleSolver, WrongInputException

class PuzzleSolverTest(unittest.TestCase):
    def test_result_type(self):
        input_list = [
            ['C','A','T'],
            ['X','Z','T'],
            ['Y','O','T']]

        ps = PuzzleSolver(input_list)
        result = ps.findWords()
        self.assertIsInstance(result, int)

    def test_findWordInCharList(self):
        input_list = [['C','A','T','A','C']]        
        ps = PuzzleSolver(input_list)
        result = ps.findWordInCharList('AT',ps.input_list[0])
        self.assertEqual(result, 2)

    def test_result_true(self):
        input_list = [
            ['C','A','T'],
            ['X','Z','T'],
            ['Y','O','T']]

        ps = PuzzleSolver(input_list)
        result = ps.findWords()                
        self.assertEqual(result, 8)

class PuzzleSolverInputTest(unittest.TestCase):

    def test_input_ok(self):
        input_list = [
            ['X', 'Z', 'T', 'A', 'T', 'Z'],
            ['C', 'A', 'O', 'C', 'A', 'T'],
            ['Y', 'O', 'T', 'H', 'A', 'Y'],
            ['X', 'Z', 'T', 'A', 'T', 'Z'],
            ['I', 'D', 'N', 'K', 'S', 'J'],
            ['G', 'W', 'E', 'O', 'P', 'K']]
        self.assertIsInstance(PuzzleSolver(input_list), PuzzleSolver)
   
    def test_input_type(self):
        input_list = 'String'
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(input_list)

        exception = contextManager.exception
        self.assertEqual(exception.code, 0)

    def test_input_row_type(self):
        input_list = [            
            ['C', 'A', 'O', 'C', 'A', 'T'],
            'OK',
            ['Y', 'O', 'T', 'H', 'A', 'Y']]
            
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(input_list)

        exception = contextManager.exception
        self.assertEqual(exception.code, 1)

    def test_input_row_length(self):
        input_list = [            
            ['C', 'A', 'O', 'C', 'A', 'T'],
            ['OK'],
            ['Y', 'O', 'T', 'H', 'A', 'Y']]
            
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(input_list)

        exception = contextManager.exception
        self.assertEqual(exception.code, 2)

    def test_input_char_type(self):
        input_list = [
            ['X', 1, 'T'],
            ['C', 'A', 'O'],
            ['Y', 'O', 'T']]
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(input_list)

        exception = contextManager.exception
        self.assertEqual(exception.code, 3)

    def test_input_char_alpha(self):
        input_list = [
            ['X', '1', 'T'],
            ['C', 'A', 'O'],
            ['Y', 'O', 'T']]
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(input_list)

        exception = contextManager.exception
        self.assertEqual(exception.code, 4)

    def test_input_char_length(self):
        input_list = [
            ['X', 'AS', 'T'],
            ['C', 'A', 'O'],
            ['Y', 'O', 'T']]
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(input_list)

        exception = contextManager.exception
        self.assertEqual(exception.code, 5)

if __name__ == '__main__':
    unittest.main()
