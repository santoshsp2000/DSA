# 1232. Check If It Is a Straight Line
# Leetcode Easy
# Date: 5 June 2023
# TC: O(N)
# SC: O(1)
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        ans = True
        pre = None

        for i in range(1, n):
            num = (coordinates[i][1] - coordinates[i - 1][1])
            denom = (coordinates[i][0] - coordinates[i - 1][0])
            if denom == 0:
                m = float('inf')
            else: m = num / denom
            if not pre: pre = m
            else: ans = ans and pre == m

        return ans
