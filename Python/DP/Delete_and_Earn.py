# 740. Delete and Earn ---- leetcode
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        # Tabulation  + Space optimized code

        n = max(nums)
        arr = [0] * (n + 1)

        for i in range(len(nums)):
            arr[nums[i]] += 1

        if n == 1: return arr[1]
        a, b = arr[1], max(arr[1], arr[2] * 2)

        for i in range(3, n + 1):
            temp = max(arr[i] * i + a, b)
            a, b = b, temp
        return b
