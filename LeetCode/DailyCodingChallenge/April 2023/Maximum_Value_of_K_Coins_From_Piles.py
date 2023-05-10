# 2218. Maximum Value of K Coins From Piles
# Leetcode Hard
# Date: 15 April 2023
# TC: O(N^2)
# SC: O(N^2)


class Solution:
    def maxValueOfCoins(self, piles, k):

        dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]

        for i in range(1, len(piles) + 1):

            for j in range(1, k + 1):

                cur = 0

                for x in range(min(len(piles[i - 1]), j)):

                    cur += piles[i - 1][x]

                    dp[i][j] = max(dp[i][j], cur + dp[i - 1][j - x - 1])

                dp[i][j] = max(dp[i][j], dp[i - 1][j])

        return dp[len(piles)][k]