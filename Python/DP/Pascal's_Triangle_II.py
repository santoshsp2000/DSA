# 119. Pascal's Triangle II ---- leetcode
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        ans = [1]
        num = 1

        for i in range(1, rowIndex+1):
            num *= (rowIndex+1-i)
            num //= i
            ans.append(num)
        return ans
