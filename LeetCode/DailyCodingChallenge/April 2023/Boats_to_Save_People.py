# 881. Boats to Save People
# Leetcode Medium
# Date: 3 April 2023
# TC: O(nlog(n))
# SC: O(1)
# Two Pointer Approach
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        i = 0
        j = n - 1
        ans = 0
        people.sort()

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            ans += 1

        return ans
