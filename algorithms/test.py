import numpy as np

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)