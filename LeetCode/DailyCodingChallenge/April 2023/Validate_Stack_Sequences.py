# 946. Validate Stack Sequences
# Leetcode Medium
# Date: 13 April 2023
# TC: O(N)
# SC: O(N)
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        arr = []
        n = len(pushed)
        i = 0
        j = 0

        while i < n:
            if arr and arr[-1] == popped[j]:
                arr.pop()
                j += 1
            elif popped[j] == pushed[i]:
                j += 1
                i += 1
            else:
                arr.append(pushed[i])
                i += 1

        while arr and j < n:
            if arr[-1] == popped[j]:
                arr.pop()
            else:
                break
            j += 1

        if arr: return False
        return True
