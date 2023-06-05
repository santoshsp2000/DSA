# 1456. Maximum Number of Vowels in a Substring of Given Length
# Leetcode Medium
# Date: 5 May 2023
# TC: O(N)
# SC: O(1)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        n = len(s)
        i, j = 0, 0
        maxx = 0
        count = 0

        while j < n:
            if s[j] in d:
                count += 1
            if j - i >= k:
                if s[i] in d:
                    count -= 1
                i += 1
            if maxx < count:
                maxx = count
            j += 1

        return maxx
