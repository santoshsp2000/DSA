# 118. Pascal's Triangle ---- leetcode
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        n = numRows
        for i in range(1, n):
            num = 1
            cur = [1]
            for j in range(1, i+1):
                num *= (i+1-j)
                num //= j
                cur.append(num)
            ans.append(cur)
        return ans
