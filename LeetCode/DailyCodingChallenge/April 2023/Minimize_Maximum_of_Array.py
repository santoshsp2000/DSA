# 2439. Minimize Maximum of Array
# Leetcode Medium
# Date: 5 April 2023
# TC: O(N)
# SC: O(1)
from typing import List


class Solution:

    def minimizeArrayValue(self, nums: List[int]) -> int:
        summ = 0
        result = 0
        for i in range(len(nums)):
            summ += nums[i]
            result = max(result, (summ + i) // (i + 1))

        return result
