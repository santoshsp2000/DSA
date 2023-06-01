# 1091. Shortest Path in Binary Matrix
# Leetcode Medium
# Date: 1 June 2023
# TC: O(N^2)
# SC: O(N^2)
from typing import List
from collections import deque


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        X = [-1, -1, -1, 0, 0, 1, 1, 1]
        Y = [-1, 0, 1, -1, 1, -1, 0, 1]
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        que = deque()
        que.append((0, 0, 1))

        while que:
            i, j, time = que.popleft()
            if i == n-1 and j == n-1: return time
            for k in range(8):
                x = i + X[k]
                y = j + Y[k]
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    que.append((x, y, time+1))
                    grid[x][y] = 2
        return -1
