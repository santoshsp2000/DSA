# 1639. Number of Ways to Form a Target String Given a Dictionary
# Leetcode Hard
# Date: 16 April 2023
# TC: O(N^M)
# SC: O(N)
from typing import List


class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        m, n = len(words), len(words[0])

        # frequency array for each character in each column
        freq = [[0] * 26 for _ in range(n)]
        for j in range(n):
            for i in range(m):
                freq[j][ord(words[i][j]) - ord('a')] += 1

        # dp array to store the number of ways to form the prefix of target
        dp = [1] + [0] * len(target)

        # fill dp array from left to right
        for j in range(n):
            for i in range(len(target), 0, -1):
                dp[i] += dp[i - 1] * freq[j][ord(target[i - 1]) - ord('a')]
                dp[i] %= mod

        return dp[len(target)]