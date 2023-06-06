# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# Leetcode Medium
# Date: 6 May 2023
# TC: O(N * log(N))
# SC: O(1)
from typing import List


class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        i, j, ans = 0, n-1, 0

        while i <= j:
            if nums[i] + nums[j] <= target:
                ans += 2**(j-i)
                ans = ans%(10**9+7)
                i += 1
            else:
                j -= 1

        return ans
