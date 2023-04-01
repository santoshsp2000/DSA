# 704. Binary Search
# Leetcode Easy
# Date: 1 April 2023
# TC: O(log(n))
# SC: O(1)
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        return -1
