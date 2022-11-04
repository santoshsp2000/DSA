from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """   Do not return anything, modify nums in-place instead.  """

        n = len(nums)
        if n == 1: return nums

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break

        for j in range(n - 1, -1, -1):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                break

        j = n - 1

        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums
