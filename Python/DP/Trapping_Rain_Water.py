# 42. Trapping Rain Water ---- leetcode
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0
        arr = [0] * n
        maxx = height[0]
        for i in range(1, n):
            maxx = max(maxx, height[i])
            arr[i] = maxx

        maxx = height[n - 1]
        for i in range(n - 2, 0, -1):
            maxx = max(maxx, height[i])
            arr[i] = min(maxx, arr[i])

        summ = 0
        for i in range(1, n - 1):
            summ += arr[i] - height[i]
        return summ

