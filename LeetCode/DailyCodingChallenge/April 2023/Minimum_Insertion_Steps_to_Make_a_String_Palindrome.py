# 1312. Minimum Insertion Steps to Make a String Palindrome
# Leetcode Hard
# Date: 22 April 2023
# TC: O(N ^ 2)
# SC: O(N ^ 2)


class Solution:
    def find(self, s, i, j, dp):
        if i >= j:
            return 0
        elif dp[i][j] != -1:
            return dp[i][j]

        if s[i] == s[j]:
            dp[i][j] = self.find(s, i + 1, j - 1, dp)
        else:
            dp[i][j] = 1 + min(self.find(s, i + 1, j, dp), self.find(s, i, j - 1, dp))
        return dp[i][j]

    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for i in range(n)] for j in range(n)]
        return self.find(s, 0, n - 1, dp)
