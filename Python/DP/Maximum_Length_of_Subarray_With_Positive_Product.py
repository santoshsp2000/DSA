# 1567. Maximum Length of Subarray With Positive Product ---- leetcode
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] > 0: return 1
            return 0
        for i in range(n):
            if nums[i] > 0:
                nums[i] = 2
            elif nums[i] < 0:
                nums[i] = -2

        maxx = 1
        minn = 1
        ans = 0

        for i in range(n):
            if nums[i] < 0:
                maxx, minn = minn, maxx

            maxx = max(maxx * nums[i], nums[i])
            minn = min(minn * nums[i], nums[i])
            ans = max(ans, maxx)
        llen = 0
        while ans > 1:
            llen += 1
            ans = ans >> 1
        return llen