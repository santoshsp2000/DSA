# 1046. Last Stone Weight
# Leetcode Easy
# Date: 24 April 2023
# TC: O(N)
# SC: O(N)
import heapq as hp
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        hp.heapify(stones)
        n = len(stones)

        while stones:
            if n == 1:
                return -stones[0]
            x = -hp.heappop(stones)
            y = -hp.heappop(stones)
            if x == y:
                n -= 2
            else:
                hp.heappush(stones, -(x - y))
                n -= 1

        return 0
