# 1611. Minimum One Bit Operations to Make Integers Zero
# Leetcode Hard
# Date: 30 November 2023
# TC: O(log(N))
# SC: O(log(n))


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        if n <= 1:
            return n

        count = 0
        while (1 << count) <= n:
            count += 1

        return ((1 << count) - 1) - self.minimumOneBitOperations(n - (1 << (count - 1)))
