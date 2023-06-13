# 2352. Equal Row and Column Pairs
# Leetcode Medium
# Date: 13 June 2023
# TC: O(N^3)
# SC: O(1)
from typing import List


class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if grid[k][j] != grid[i][k]: break
                else:
                    count += 1

        return count
