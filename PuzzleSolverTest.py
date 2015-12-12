# coding=utf-8

import unittest
from PuzzleSolver import PuzzleSolver, WrongInputException


class PuzzleSolverTest(unittest.TestCase):
    def test_result_type(self):
        puzzle = [
            ['C', 'A', 'T'],
            ['X', 'Z', 'T'],
            ['Y', 'O', 'T']]

        ps = PuzzleSolver(puzzle)
        result = ps.findWords()
        self.assertIsInstance(result, int)

    def test_findWordInString(self):
        string = 'CATAPULT'
        result = PuzzleSolver.findWordInString('AT', string)
        self.assertEqual(result, 2)

    def test_getStringList(self):
        puzzle = [
            ['C', 'A', 'T'],
            ['X', 'Z', 'T'],
            ['Y', 'O', 'T']]

        puzzle_2 = [
            ['C', 'A', 'T', 'A', 'P', 'U', 'L', 'T'],
            ['X', 'Z', 'T', 'T', 'O', 'Y', 'O', 'O'],
            ['Y', 'O', 'T', 'O', 'X', 'T', 'X', 'X']]


        ps = PuzzleSolver(puzzle)
        ps2 = PuzzleSolver(puzzle_2)

        result = ['CAT', 'XZT', 'YOT', 'CXY', 'AZO', 'TTT', 'CZT', 'AT', 'XO', 'TO', 'TZY', 'AX']
        result2 = [
            'CATAPULT', 'XZTTOYOO', 'YOTOXTXX',
            'CXY', 'AZO', 'TTT', 'ATO', 'POX', 'UYT', 'LOX',
            'TOX', 'PYX', 'TTX', 'XO', 'ATO', 'UOX', 'CZT',
            'AOT', 'LO', 'TZY', 'ATO', 'LYX', 'TOT', 'OX',
            'AX', 'PTT', 'UOO']

        self.assertEqual(set(ps.getStringList()), set(result))
        self.assertEqual(set(ps2.getStringList()), set(result2))
        
    def test_result_true(self):
        puzzle_list = [
            [
                ['C', 'A', 'T'],
                ['X', 'Z', 'T'],
                ['Y', 'O', 'T']
            ],
            [
                ['C', 'A', 'T', 'A', 'P', 'U', 'L', 'T', 'M'],
                ['X', 'Z', 'T', 'T', 'O', 'Y', 'O', 'O', 'S'],
                ['Y', 'O', 'T', 'O', 'X', 'T', 'X', 'X', 'D'],
            ],
            [
                ['C', 'A', 'T', 'A', 'P', 'U', 'L', 'T', 'M'],
                ['X', 'Z', 'T', 'T', 'O', 'Y', 'O', 'O', 'S'],
                ['Y', 'O', 'T', 'O', 'X', 'T', 'X', 'X', 'D'],
                ['C', 'A', 'T', 'A', 'P', 'U', 'L', 'T', 'M'],
                ['X', 'Z', 'T', 'T', 'O', 'Y', 'O', 'O', 'S'],
                ['Y', 'O', 'T', 'O', 'X', 'T', 'X', 'X', 'D'],
                ['C', 'A', 'T', 'A', 'P', 'U', 'L', 'T', 'M'],
                ['X', 'X', 'T', 'T', 'O', 'Y', 'O', 'O', 'S'],
                ['Y', 'O', 'T', 'O', 'X', 'T', 'Y', 'X', 'D']
            ]
        ]

        puzzle_list.append(zip(*puzzle_list[1][::-1]))
        puzzle_list.append(list(reversed(zip(*puzzle_list[1]))))

        for puzzle in puzzle_list:
            for index, puzzle in enumerate(puzzle_list):
                ps = PuzzleSolver(puzzle)
                if index == 0:
                    self.assertEqual(ps.findWords(), 8)
                elif index in [1, 3, 4]:
                    self.assertEqual(ps.findWords(), 22)
                else:
                    self.assertEqual(ps.findWords(), 69)
   


class PuzzleSolverInputTest(unittest.TestCase):

    def test_input_ok(self):
        puzzle = [
            ['X', 'Z', 'T', 'A', 'T', 'Z'],
            ['C', 'A', 'O', 'C', 'A', 'T'],
            ['Y', 'O', 'T', 'H', 'A', 'Y']]
        self.assertIsInstance(PuzzleSolver(puzzle), PuzzleSolver)
   
    def test_input_type(self):
        puzzle = 'String'
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(puzzle)

        exception = contextManager.exception
        self.assertEqual(exception.code, 0)

    def test_input_row_type(self):
        puzzle = [            
            ['C', 'A', 'O', 'C', 'A', 'T'],
            'OK',
            ['Y', 'O', 'T', 'H', 'A', 'Y']]
            
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(puzzle)

        exception = contextManager.exception
        self.assertEqual(exception.code, 1)

    def test_input_row_length(self):
        puzzle = [
            ['C', 'A', 'O', 'C', 'A', 'T'],
            ['OK'],
            ['Y', 'O', 'T', 'H', 'A', 'Y']]
            
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(puzzle)

        exception = contextManager.exception
        self.assertEqual(exception.code, 2)

    def test_input_char_type(self):
        puzzle = [
            ['X', 1, 'T'],
            ['C', 'A', 'O'],
            ['Y', 'O', 'T']]
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(puzzle)

        exception = contextManager.exception
        self.assertEqual(exception.code, 3)

    def test_input_char_alpha(self):
        puzzle = [
            ['X', '1', 'T'],
            ['C', 'A', 'O'],
            ['Y', 'O', 'T']]
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(puzzle)

        exception = contextManager.exception
        self.assertEqual(exception.code, 4)

    def test_input_char_length(self):
        puzzle = [
            ['X', 'AS', 'T'],
            ['C', 'A', 'O'],
            ['Y', 'O', 'T']]
        with self.assertRaises(WrongInputException) as contextManager:
            PuzzleSolver(puzzle)

        exception = contextManager.exception
        self.assertEqual(exception.code, 5)

if __name__ == '__main__':
    unittest.main()
