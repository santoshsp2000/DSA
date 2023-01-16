# 198. House Robber ---- leetcode
from typing import List


class Solution:
    # Recursive Approach
    def find(self, n, nums, dp):
        if n < 0:
            return 0
        elif dp[n] != -1:
            return dp[n]
        dp[n] = max(nums[n] + self.find(n - 2, nums, dp), self.find(n - 1, nums, dp))
        return dp[n]

    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [-1] * n
        # return self.find(n-1, nums, dp)                       # Calling recursive method


        # Tabulation Approach

        # n = len(nums)
        # if n == 1: return nums[0]
        # dp = [0] * n

        # for i in range(n):
        #     if i == 0:
        #         dp[i] = nums[i]
        #     elif i == 1:
        #         dp[i] = max(dp[i-1], nums[i])
        #     else:
        #         dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        # return max(dp[n-1], dp[n-2])


        # Space optimized code

        n = len(nums)
        if n == 1: return nums[0]
        a = nums[0]
        b = max(a, nums[1])

        for i in range(2, n):
            temp = max(nums[i] + a, b)
            a, b = b, temp
        return b
