# 2390. Removing Stars From a String
# Leetcode Medium
# Date: 11 April 2023
# TC: O(N)
# SC: O(N)


class Solution:

    def removeStars(self, s: str) -> str:
        arr = []

        for i in s:
            if i == '*':
                arr.pop()
            else:
                arr.append(i)
        s = ""
        for i in arr:
            s += i
        return s
