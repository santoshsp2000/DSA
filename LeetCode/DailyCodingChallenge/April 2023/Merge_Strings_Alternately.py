# 1768. Merge Strings Alternately
# Leetcode Easy
# Date: 18 April 2023
# TC: O(N+M)
# SC: O(N+M)


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        s = ''
        n = len(word1)
        m = len(word2)
        i, j = 0, 0
        count = 0

        while i < n and j < m:

            if count % 2 == 0:
                s += word1[i]
                i += 1
            else:
                s += word2[j]
                j += 1
            count += 1

        while i < n:
            s += word1[i]
            i += 1

        while j < m:
            s += word2[j]
            j += 1

        return s