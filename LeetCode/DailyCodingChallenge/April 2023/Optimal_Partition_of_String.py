# 2405. Optimal Partition of String
# Leetcode Medium
# Date: 3 April 2023
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:

    def partitionString(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        letters = {}
        ans = 0

        while j < n:
            if s[j] in letters:
                letters[s[j]] += 1
            else:
                letters[s[j]] = 1

            if letters[s[j]] > 1:
                while i < j:
                    if s[i] == s[j]:
                        ans += 1
                    letters[s[i]] -= 1
                    i += 1

            j += 1

        if i != j:
            ans += 1

        return ans
