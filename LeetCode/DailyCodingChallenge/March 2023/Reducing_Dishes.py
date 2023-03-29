# 1402. Reducing Dishes
from typing import List


class Solution:

    def find(self, n, ind, time, satisfaction, dp):
        if ind == n or time > n:
            return 0
        elif dp[ind][time] != -1:
            return dp[ind][time]

        dp[ind][time] = max(satisfaction[ind] * time + self.find(n, ind + 1, time + 1, satisfaction, dp),
                            self.find(n, ind + 1, time, satisfaction, dp))

        return dp[ind][time]

    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        n = len(satisfaction)
        dp = [[-1 for i in range(n + 1)] for j in range(n + 1)]

        return self.find(n, 0, 1, satisfaction, dp)
