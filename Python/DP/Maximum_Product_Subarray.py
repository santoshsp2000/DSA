# 152. Maximum Product Subarray ---- leetcode
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force approach

        # maxx = float('-inf')
        # n = len(nums)
        # for i in range(n):
        #     prod = 1
        #     for j in range(i, n):
        #         prod *= nums[j]
        #         maxx = max(maxx, prod)
        # return maxx


        # Optimized Approach
        maxx = nums[0]
        minn = nums[0]
        ans = nums[0]
        n = len(nums)
        if n == 1: return nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                maxx, minn = minn, maxx

            maxx = max(maxx *nums[i], nums[i])
            minn = min(minn *nums[i], nums[i])
            ans = max(ans, maxx)
        return ans