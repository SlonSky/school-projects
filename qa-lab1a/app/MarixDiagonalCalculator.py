""" Lab1a problem resolver class """


class MatrixDiagonalCalculator(object):
    """ On given matrix, switches max diagonal and min column elements """

    def calculate(self, matrix, column):
        """ Make main and singular calculation """

        self._validate(matrix, column)

        max_diagonal_x, max_diagonal_y = self._find_max_diagonal(matrix)
        min_column_x, min_column_y = self._find_min_at_column(column, matrix)

        result = list(map(list, matrix))

        result[max_diagonal_y][max_diagonal_x] = matrix[min_column_y][min_column_x]
        result[min_column_y][min_column_x] = matrix[max_diagonal_y][max_diagonal_x]

        return result

    def _validate(self, matrix, column):
        if not matrix:
            raise ValueError('Matrix must not be empty')

        if column < 0:
            raise ValueError('Column number must be grater than 0')

    def _find_max_diagonal(self, matrix):
        diag_size = min(len(matrix), len(matrix[0]))

        max_value = matrix[0][0]
        max_pos = 0

        for i in range(diag_size):
            if matrix[i][i] > max_value:
                max_value = matrix[i][i]
                max_pos = i

        return max_pos, max_pos

    def _find_min_at_column(self, column, matrix):
        height = len(matrix)

        min_value = matrix[0][column]
        min_pos = 0

        for i in range(height):
            if matrix[i][column] < min_value:
                min_value = matrix[i][i]
                min_pos = i

        return column, min_pos
