# 2187. Minimum Time to Complete Trips
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)
        l = 1
        h = totalTrips * min(time)

        while l < h:
            mid = (l + h) >> 1
            total = 0
            for j in range(n):
                total += mid//time[j]
            if total < totalTrips:
                l = mid + 1
            else:
                h = mid

        return l