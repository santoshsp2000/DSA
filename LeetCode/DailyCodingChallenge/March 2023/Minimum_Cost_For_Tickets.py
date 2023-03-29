# 983. Minimum Cost For Tickets
from typing import List


class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        dp = [365*costs[0]] * (n+1)
        dp[0] = 0

        for i in range(n):
            d7, d30 = i, i

            while d7 >= 0 and days[d7] > days[i] - 7: d7 -= 1
            while d30 >= 0 and days[d30] > days[i] - 30: d30 -= 1

            dp[i+1] = min(costs[0] + dp[i], costs[1] + dp[d7+1], costs[2] + dp[d30+1])

        return dp[n]
