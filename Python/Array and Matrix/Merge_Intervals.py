from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        ans = []

        for inter in intervals:
            if ans and ans[-1][1] >= inter[0]:
                ans[-1][1] = max(inter[1], ans[-1][1])
            else:
                ans.append(inter)

        return ans