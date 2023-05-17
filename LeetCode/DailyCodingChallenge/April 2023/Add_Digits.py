# 258. Add Digits
# Leetcode Easy
# Date: 26 April 2023
# TC: O(1)
# SC: O(1)


class Solution:

    def addDigits(self, num: int) -> int:
        if num == 0: return num
        return num%9 if num%9 != 0 else 9
