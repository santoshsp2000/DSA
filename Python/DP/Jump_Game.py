# 55. Jump Game ---- leetcode
from typing import List


class Solution:
    # Recursive Approach
    def find(self, n, ind, nums, dp):
        if n - 1 <= ind:
            return True
        elif dp[ind] != -1:
            return dp[ind]
        ans = False
        for i in range(nums[ind], 0, -1):
            ans = ans or self.find(n, ind + i, nums, dp)
        dp[ind] = ans
        return ans

    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # dp = [-1] * n
        # return self.find(n, 0, nums, dp)                      # Calling recursive method


        # Optimized Approach
        n = len(nums)
        if n == 1:
            return True
        elif nums[0] == 0:
            return False
        ladder = nums[0]
        steps = nums[0]

        for i in range(1, n):
            if i == n - 1: return True
            if i + nums[i] > ladder:
                ladder = i + nums[i]
            steps -= 1
            if steps == 0:
                steps = ladder - i
                if steps == 0:
                    return False
