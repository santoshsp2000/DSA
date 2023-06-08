# 1318. Minimum Flips to Make a OR b Equal to c
# Leetcode Medium
# Date: 7 June 2023
# TC: O(31)
# SC: O(1)


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while c != 0 or a != 0 or b != 0:
            if c & 1 == 1:
                if not a&1 and not b&1:
                    count += 1
            else:
                count += (a&1) + (b&1)
            c = c>>1
            a = a>>1
            b = b>>1

        return count