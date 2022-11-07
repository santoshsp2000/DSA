from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictn = {}

        for i in range(len(nums)):
            if target - nums[i] in dictn:
                return [dictn[target - nums[i]], i]
            else:
                dictn[nums[i]] = i
