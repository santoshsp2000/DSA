# 2444. Count Subarrays With Fixed Bounds
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        start = 0
        min_ind = 0
        max_ind = 0
        is_min = False
        is_max = False
        ans = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                is_min = False
                is_max = False
                start = i + 1

            if nums[i] == minK:
                is_min = True
                min_ind = i

            if nums[i] == maxK:
                is_max = True
                max_ind = i

            if is_max and is_min:
                ans += min(max_ind, min_ind) - start + 1

        return ans