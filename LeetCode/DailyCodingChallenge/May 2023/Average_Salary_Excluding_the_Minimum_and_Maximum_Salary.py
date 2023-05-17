# 1491. Average Salary Excluding the Minimum and Maximum Salary
# Leetcode Easy
# Date: 1 May 2023
# TC: O(N)
# SC: O(1)
from typing import List


class Solution:

    def average(self, salary: List[int]) -> float:
        maxx = 1000
        minn = 1000000
        ans = 0
        n = 0

        for i in salary:
            if i > maxx:
                maxx = i
            if i < minn:
                minn = i
            ans += i
            n += 1
        return (ans-maxx-minn)/(n-2)
