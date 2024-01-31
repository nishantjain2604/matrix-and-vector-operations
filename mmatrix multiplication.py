print("RegNo 2367413  Name:Nishant    Prog:Matrix Multiplication")
def matrix_mult(matrix1, matrix2):
        rowsA = len(matrix1)
        colsA = len(matrix1[0])
        rowsB = len(matrix2)
        colsB = len(matrix2[0])
        if colsA != rowsB:
            return "Cannot Multiply!"
        else:
            result = [[0 for row in range(colsB)] for col in range(rowsA)]
            for i in range(rowsA):
                for j in range(colsB):
                    for k in range(colsA):
                        result[i][j] += matrix1[i][k] * matrix2[k][j]
            return result

matrixA = [[2,3,1], [3,3,1], [2,4,1]]
matrixB = [[1,6,2], [-1,-1,-4], [2,-11,11]]
print("matrix A=",matrixA)
print("matrix B=",matrixB)
print("Matrix A* Matrix B=",matrix_mult(matrixA, matrixB))

2
3
1
3
3
1
2
4
1