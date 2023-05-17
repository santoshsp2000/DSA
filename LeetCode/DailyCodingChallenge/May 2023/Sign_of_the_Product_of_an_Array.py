# 1822. Sign of the Product of an Array
# Leetcode Easy
# Date: 2 May 2023
# TC: O(N)
# SC: O(1)
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            ans *= i
        if ans == 0:
            return 0
        elif ans > 0:
            return 1
        return -1
