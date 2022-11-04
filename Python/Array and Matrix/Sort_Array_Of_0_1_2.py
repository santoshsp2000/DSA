from typing import List


class Solution:

    def sort_arry012(self, nums: List[int]) -> None:
        """ Do not return anything, modify nums in-place instead. """

        start, mid = 0, 0
        end = len(nums) - 1

        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                mid += 1
                start += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            else:
                mid += 1
