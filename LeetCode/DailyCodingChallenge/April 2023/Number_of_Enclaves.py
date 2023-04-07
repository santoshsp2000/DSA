# 1020. Number of Enclaves
# Leetcode Medium
# Date: 7 April 2023
# TC: O(N^2)
# SC: O(1)
from typing import List


X = [-1, 0, 0, 1]
Y = [0, -1, 1, 0]


class Solution:
    def check_and_count(self, n, m, i, j, grid, count):
        if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 1:
            return count, False

        grid[i][j] = -1
        count += 1
        status = True

        for k in range(4):
            x = i + X[k]
            y = j + Y[k]

            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                cnt, sts = self.check_and_count(n, m, x, y, grid, count)
                count = max(count, cnt)
                status &= sts

        return count, status

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count, status = self.check_and_count(n, m, i, j, grid, 0)
                    if status:
                        ans += count

        return ans
