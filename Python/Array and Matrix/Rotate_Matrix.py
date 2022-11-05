from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """        Do not return anything, modify matrix in-place instead.        """

        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            j = 0
            k = n - 1

            while j <= k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1
