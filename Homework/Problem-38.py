#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. 

def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False
    col_zero = False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                if i == 0:
                    row_zero = True
                if j == 0:
                    col_zero = True
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    if col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  #output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]