# 1431. Kids With the Greatest Number of Candies
# Leetcode Easy
# Date: 17 April 2023
# TC: O(N)
# SC: O(N)
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= maxx:
                ans.append(True)
            else:
                ans.append(False)
        return ans