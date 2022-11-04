from typing import List


class Solution:

    def max_profit(self, prices: List[int]) -> int:
        maxx = 0
        minn = prices[0]

        for ele in prices:
            if ele < minn:
                minn = ele
            elif maxx < ele - minn:
                maxx = ele - minn

        return maxx