# 509. Fibonacci Number
# Leetcode Easy
# Date: 6 April 2023
# TC: O(N)
# SC: O(1)


class Solution:

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(n - 1):
            temp = a + b
            a, b = b, temp

        return b
