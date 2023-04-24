# 374. Guess Number Higher or Lower
# Leetcode Easy
# Date: 24 April 2023
# TC: O(log(N))
# SC: O(1)


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:

    def guessNumber(self, n: int) -> int:
        l = 1
        h = n

        while l <= h:
            mid = (l + h) >> 1
            res = guess(mid)
            if 0 == res:
                return mid
            elif 1 == res:
                l = mid + 1
            else:
                h = mid - 1
