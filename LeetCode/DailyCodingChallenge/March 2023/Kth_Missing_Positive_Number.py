# 1539. Kth Missing Positive Number
from typing import List


class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            d[i] = i

        i = 1
        while True:
            if i not in d:
                k -= 1
                if k == 0:
                    return i
            i += 1
