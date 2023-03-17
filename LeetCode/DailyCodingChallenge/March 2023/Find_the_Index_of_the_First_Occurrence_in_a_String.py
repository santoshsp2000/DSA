# 28. Find the Index of the First Occurrence in a String


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        lps = [0] * m
        i, j = 0, 1

        while j < m:
            if needle[i] == needle[j]:
                lps[j] = i + 1
                j += 1
                i += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]

        i, j = 0, 0

        while i < n and j < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]

            if j == m: return i - j
        return -1
