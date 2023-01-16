# 918. Maximum Sum Circular Subarray ---- leetcode
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxx = nums[0]
        summ = 0

        for i in nums:
            summ += i
            if maxx < summ:
                maxx = summ
            if summ < 0:
                summ = 0

        minn = nums[0]
        summ = 0

        for i in nums:
            summ += i
            if minn > summ:
                minn = summ
            if summ > 0:
                summ = 0
        summ = sum(nums)
        if minn == summ: return maxx
        return max(maxx, summ - minn)
