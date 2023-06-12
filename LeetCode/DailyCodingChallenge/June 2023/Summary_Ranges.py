# 228. Summary Ranges
# Leetcode Easy
# Date: 12 June 2023
# TC: O(N)
# SC: O(N)
from typing import List


class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        d = {i: i for i in nums}

        for i in nums:
            if i - 1 not in d:
                s = str(i)
                j = i
                while j in d:
                    j += 1
                if i != j - 1: s += '->' + str(j - 1)
                ans.append(s)

        return ans
