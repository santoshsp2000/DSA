# 1351. Count Negative Numbers in a Sorted Matrix
# Leetcode Easy
# Date: 8 June 2023
# TC: O(N+M)
# SC: O(1)
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        i, j = 0, m - 1
        count = 0

        while i < n and j >= 0:
            if grid[i][j] < 0:
                j -= 1
            else:
                count += m - j - 1
                i += 1

        while i < n:
            count += m
            i += 1

        return count