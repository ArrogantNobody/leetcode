# import numpy as np
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         matrix = np.array(matrix)
#         matrix = matrix.T
#         matrix = matrix.tolist()
#         for item in matrix:
#             item.reverse()
#         return matrix

#normal version
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for item in matrix:
            item.reverse()

        return matrix