# 122. Best Time to Buy and Sell Stock II ---- leetcode
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        ans = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans
