# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.


def zero(matrix):
    row_flag = [False] * len(matrix)
    col_flag = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 0):
                row_flag[i] = True
                col_flag[j] = True

    for i in range(len(row_flag)):
        if (row_flag[i]):
            zero_row(matrix, i)

    for i in range(len(col_flag)):
        if (col_flag[i]):
            zero_col(matrix, i)


def zero_row(matrix, index):
    for i in range(len(matrix[0])):
        matrix[index][i] = 0


def zero_col(matrix, index):
    for i in range(len(matrix)):
        matrix[i][index] = 0


def zero_answer(matrix):
    row_has_zero = False
    col_has_zero = False

    for i in range(len(matrix)):
        if (matrix[i][0] == 0):
            col_has_zero = True
            break

    for i in range(len(matrix[0])):
        if (matrix[0][i] == 0):
            row_has_zero = True
            break

    for i in range(1, len(matrix), 1):
        for j in range(1, len(matrix[0]), 1):
            if (matrix[i][j] == 0):
                matrix[0][j] = 0
                matrix[i][0] = 0
    
    for i in range(1, len(matrix), 1):
        if (matrix[i][0] == 0):
            zero_row(matrix, i)

    for i in range(1, len(matrix[0]), 1):
        if (matrix[0][i] == 0):
            zero_col(matrix, i)
    
    if (row_has_zero):
        zero_row(matrix, 0)
    
    if (col_has_zero):
        zero_col(matrix, 0)

    


matrix = [[1, 2, 4, 7], [2, 3, 0, 4], [2, 0, 5, 4]]

zero_answer(matrix)

for row in matrix:
    print(row)
