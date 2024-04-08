from .MarixDiagonalCalculator import MatrixDiagonalCalculator


def main():

    matrix = [
        [-10, 4, 12, 32, -30],
        [30, 0, 13, 5, -88],
        [1, 65, -23, 991, 4],
        [0, 42, 17, 43, 3],

    ]

    calculator = MatrixDiagonalCalculator()

    handle_input(calculator, matrix)


def handle_input(calculator, matrix):

    while True:

        print('Source matrix: \n', '\n'.join(map(str, matrix)), '\n')

        option = input('1-act\n2-exit\n')

        if option == '2':
            return
        elif option == '1':

            while True:
                try:
                    column = int(input('Enter column index (0-n): '))
                    result = calculator.calculate(matrix, column)

                    print('Result:\n', '\n'.join(map(str, result)))
                    break

                except ValueError as e:
                    print('Wrong input. Try again.')

if __name__ == '__main__':
    main()