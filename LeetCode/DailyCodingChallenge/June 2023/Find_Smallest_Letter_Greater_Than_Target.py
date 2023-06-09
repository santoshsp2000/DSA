# 744. Find Smallest Letter Greater Than Target
# Leetcode Easy
# Date: 9 June 2023
# TC: O(log(N))
# SC: O(1)
from typing import List


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]: return letters[0]
        ans = letters[-1]
        l, h = 0, len(letters) - 1

        while l <= h:
            mid = (l + h) >> 1
            if target < letters[mid] <= ans:
                ans = letters[mid]
                h = mid - 1
            else:
                l = mid + 1

        return ans
