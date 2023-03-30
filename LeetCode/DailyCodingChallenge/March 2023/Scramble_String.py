# 87. Scramble String


class Solution:
    def scramble(self, s1, s2, dp):
        if len(s1) == 1: return s1 == s2
        if s1 == s2: return True

        key = s1 + s2
        if key in dp: return dp[key]
        dp[key] = False

        for i in range(1, len(s1)):
            if (self.scramble(s1[:i], s2[:i], dp) and self.scramble(s1[i:], s2[i:], dp)) or (self.scramble(s1[i:], s2[:-i], dp) and self.scramble(s1[:i], s2[-i:], dp)):
                dp[key] = True
                return True

        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 1: return s1 == s2
        dp = {}
        return self.scramble(s1, s2, dp)
