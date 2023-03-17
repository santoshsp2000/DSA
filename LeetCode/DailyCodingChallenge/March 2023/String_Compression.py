# 443. String Compression
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        k = 0
        while i < n:
            cnt = 1
            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1
                cnt += 1
            chars[k] = chars[i]
            k += 1
            if cnt > 1:
                for x in str(cnt):
                    chars[k] = x
                    k += 1
            i = j

        return k
