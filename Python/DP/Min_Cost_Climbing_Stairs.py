# 746. Min Cost Climbing Stairs ---- leetcode
from typing import List


class Solution:
    # Recursive Approach
    def climb(self, n, cost, dp):
        if n < 0:
            return 0
        elif dp[n] != -1:
            return dp[n]

        dp[n] = cost[n] + min(self.climb(n - 1, cost, dp), self.climb(n - 2, cost, dp))
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [-1] * n
        # return min(self.climb(n-1, cost, dp), self.climb(n-2,cost, dp))              # Call for recursive method


        # Tabulation Approach
        # n = len(cost)
        # dp = [float('inf')] * n
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # for i in range(2, n):
        #     dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # return min(dp[n-1], dp[n-2])


        # Space Optimized code
        n = len(cost)
        a = cost[0]
        b = cost[1]

        for i in range(2, n):
            temp = cost[i] + min(a, b)
            a, b = b, temp
        return min(a, b)
