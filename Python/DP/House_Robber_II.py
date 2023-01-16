# 213. House Robber II ---- leetcode
from typing import List


class Solution:
    # Tabulation  + Space optimized method
    def find(self, start, end, nums):
        a, b = nums[start], max(nums[start], nums[start + 1])

        for i in range(start + 2, end):
            temp = max(nums[i] + a, b)
            a, b = b, temp
        return b

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        return max(self.find(0, n - 1, nums), self.find(1, n, nums))
