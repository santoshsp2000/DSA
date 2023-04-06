# 1137. N-th Tribonacci Number
# Leetcode Easy
# Date: 6 April 2023
# TC: O(N)
# SC: O(1)


class Solution:

    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1

        a, b, c = 0, 1, 1
        for i in range(n - 2):
            temp = a + b + c
            a, b, c = b, c, temp

        return c
