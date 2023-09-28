# 905. Sort Array By Parity
# Leetcode Easy
# Date: 28 September 2023
# TC: O(N)
# SC: O(1)


from typing import List


class Solution:

    def sort_array_by_parity(self, nums: List[int]) -> List[int]:

        n = len(nums)
        i, j = 0, 0

        for i in range(n):

            if nums[i] % 2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        return nums
