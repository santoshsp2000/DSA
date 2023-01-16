# 53. Maximum Subarray ---- leetcode
from typing import List


class Solution:
    # Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        summ = 0

        for i in nums:
            summ += i
            if maxx < summ:
                maxx = summ
            if summ < 0:
                summ = 0
        return maxx
