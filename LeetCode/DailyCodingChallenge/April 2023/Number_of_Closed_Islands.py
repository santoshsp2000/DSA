# 1254. Number of Closed Islands
# Leetcode Medium
# Date: 6 April 2023
# TC: O(N^2)
# SC: O(1)
from typing import List


X = [-1, 0, 0, 1]
Y = [0, -1, 1, 0]


class Solution:

    def check(self, n, m, i, j, grid):

        if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 0:
            return False
        elif grid[i][j] != 0:
            return True

        res = True
        grid[i][j] = 2

        for k in range(4):
            x = i + X[k]
            y = j + Y[k]

            if 0 <= x < n and 0 <= y < m:
                r = self.check(n, m, x, y, grid)
                res = res and r

        return res

    def closedIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 0:
                    if self.check(n, m, i, j, grid):
                        ans += 1

        return ans
