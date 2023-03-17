# 875. Koko Eating Bananas
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        m = max(piles) * h

        while l < m:
            mid = (l + m) >> 1
            total = 0
            for i in range(n):
                total += piles[i] // mid
                if piles[i] % mid > 0:
                    total += 1

            if total > h:
                l = mid + 1
            else:
                m = mid

        return l