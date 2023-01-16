# 45. Jump Game II ---- leetcode
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        ladder = nums[0]
        steps = nums[0]
        jumps = 1

        for i in range(1, n):
            if i == n - 1: return jumps
            if ladder < i + nums[i]:
                ladder = i + nums[i]
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = ladder - i
                if steps == 0:
                    return -1
