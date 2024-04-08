import sys

import unittest
from unittest import TestCase
from app.MarixDiagonalCalculator import MatrixDiagonalCalculator


class MatrixDiagonalCalculatorTest(TestCase):

    def test_calculate_valid(self):
        in_matrix = [
            [-10, 4, 12, 32, -30],
            [30, 0, 13, 5, -88],
            [1, 65, -23, 991, 4],
            [0, 42, 17, 43, 3],
        ]

        in_column = 1

        expected = [
            [-10, 4, 12, 32, -30],
            [30, 43, 13, 5, -88],
            [1, 65, -23, 991, 4],
            [0, 42, 17, 0, 3],
        ]

        calculator = MatrixDiagonalCalculator()

        result = calculator.calculate(in_matrix, in_column)

        self.assertEqual(result, expected)

    def test_calculate_empty_matrix(self):
        in_matrix = []
        in_column = 1

        calculator = MatrixDiagonalCalculator()

        with self.assertRaises(ValueError):
            result = calculator.calculate(in_matrix, in_column)

    def test_calculate_empty_column(self):
        in_matrix = [
            [-10, 4, 12, 32, -30],
            [30, 0, 13, 5, -88],
            [1, 65, -23, 991, 4],
            [0, 42, 17, 43, 3],
        ]
        in_column = -1

        calculator = MatrixDiagonalCalculator()

        with self.assertRaises(ValueError):
            result = calculator.calculate(in_matrix, in_column)

def suite():
   suite = unittest.TestSuite()
   suite.addTests(
       unittest.TestLoader().loadTestsFromTestCase(MatrixDiagonalCalculatorTest)
   )

   return suite

 

if __name__ == '__main__':
   unittest.TextTestRunner(verbosity=2).run(suite())
