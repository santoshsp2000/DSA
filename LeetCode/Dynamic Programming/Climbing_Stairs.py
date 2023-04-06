# 70. Climbing Stairs
# Leetcode Easy
# Date: 6 April 2023


# First Approach
# TC: O(N!)
# SC: O(N) stack Space
# Recursive method

class Solution:

    def climb(self, n):
        if n <= 1: return 1
        return self.climb(n-1) + self.climb(n-2)

    def climbStairs(self, n: int) -> int:
        return self.climb(n)


# Second Approach
# TC: O(N)
# SC: O(N+N) Stack Space + Dp array
# Memorization


class Solution:
    def climb(self, n, dp):
        if n <= 1: return 1
        elif dp[n] != -1: return dp[n]
        dp[n] = self.climb(n-1, dp) + self.climb(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        return self.climb(n, dp)


# Third Approach
# TC: O(N)
# SC: O(N) Dp array
# Tabulation


class Solution:

    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# Fourth Approach
# TC: O(N)
# SC: O(1)
# Space Optimized


class Solution:

    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 1

        for i in range(2, n + 1):
            temp = prev + cur
            prev, cur = cur, temp

        return cur
