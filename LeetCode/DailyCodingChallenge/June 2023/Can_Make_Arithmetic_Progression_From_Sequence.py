# 1502. Can Make Arithmetic Progression From Sequence
# Leetcode Easy
# Date: 6 June 2023
# TC: O(N * log(N))
# SC: O(1)
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n, diff = len(arr), None
        arr.sort()

        for i in range(1, n):
            if diff == None: diff = arr[i] - arr[i-1]
            elif diff != arr[i] - arr[i-1]: return False

        return True
