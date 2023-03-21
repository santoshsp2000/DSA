# 2348. Number of Zero-Filled Subarrays
from typing import List


class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                j = i
                while j < n and nums[j] == 0:
                    total += j-i+1
                    j += 1
                i = j
            else:
                i += 1

        return total
