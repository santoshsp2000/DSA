# 70. Climbing Stairs ---- leetcode


class Solution:
    # Recursive Approach
    def climb(self, n):
        if n == 0 or n == 1:
            return 1
        return self.climb(n-1) + self.climb(n-2)

    def climbStairs(self, n: int) -> int:
        # return self.climb(n)               Call for recursive method


        # Tabulation Approach
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        #
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]


        # Space Optimized code
        if n <= 1:
            return 1
        a, b = 1, 1
        for i in range(n-1):
            temp = a + b
            a, b = b, temp
        return b
