class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        tmp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    tmp.append((i, j))
        if len(tmp) == 0:
            return matrix
        else:
            for i in tmp:
                matrix[i[0]] = [0] * len(matrix[i[0]])
                for item in matrix:
                    item[i[1]] = 0
