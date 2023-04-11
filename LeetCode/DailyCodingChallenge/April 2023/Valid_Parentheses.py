# 20. Valid Parentheses
# Leetcode Easy
# Date: 10 April 2023
# TC: O(N)
# SC: O(N)


class Solution:

    def isValid(self, s: str) -> bool:
        arr = []

        for i in s:
            if i in '({[':
                arr.append(i)
            elif not arr:
                return False
            elif (i == ')' and arr[-1] == '(') or (i == '}' and arr[-1] == '{') or (i == ']' and arr[-1] == '['):
                arr.pop()
            else:
                return False

        if arr: return False
        return True
