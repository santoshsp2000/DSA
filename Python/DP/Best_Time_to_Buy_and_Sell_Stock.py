# 121. Best Time to Buy and Sell Stock ---- leetcode
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf')
        ans = 0
        for i in prices:
            if i < minn:
                minn = i
            elif ans < i - minn:
                ans = i - minn
        return ans
