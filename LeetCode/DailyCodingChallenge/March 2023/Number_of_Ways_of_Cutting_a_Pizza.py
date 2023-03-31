# 1444. Number of Ways of Cutting a Pizza -->  leetcode hard -->  31 March 2023
from typing import List


class Solution:
    def find(self, n, m, k, i, j, presum, pizza, dp):
        if presum[i][j] == 0: return 0
        if k == 0: return 1
        if dp[k][i][j] != -1: return dp[k][i][j]
        ans = 0

        for col in range(j + 1, m):
            if presum[i][j] - presum[i][col] > 0:
                ans = (ans + self.find(n, m, k - 1, i, col, presum, pizza, dp)) % (10 ** 9 + 7)

        for row in range(i + 1, n):
            if presum[i][j] - presum[row][j] > 0:
                ans = (ans + self.find(n, m, k - 1, row, j, presum, pizza, dp)) % (10 ** 9 + 7)

        dp[k][i][j] = ans
        return ans

    def ways(self, pizza: List[str], k: int) -> int:

        n = len(pizza)
        m = len(pizza[0])
        presum = [[0 for i in range(m + 1)] for j in range(n + 1)]
        dp = [[[-1 for i in range(m + 1)] for j in range(n + 1)] for x in range(k)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                presum[i][j] = presum[i + 1][j] + presum[i][j + 1] - presum[i + 1][j + 1]
                if pizza[i][j] == 'A':
                    presum[i][j] += 1

        return self.find(n, m, k - 1, 0, 0, presum, pizza, dp)
