# 2300. Successful Pairs of Spells and Potions
# Leetcode Medium
# Date: 2 April 2023
# TC: O(nlog(n))
# SC: O(n)
from typing import List


class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        ans = []
        potions.sort()

        for i in range(n):
            j = 0
            k = m-1

            while j <= k:
                mid = (j+k)>>1
                prod = spells[i]*potions[mid]

                if prod < success:
                    j = mid+1
                else:
                    k = mid-1
            ans.append(m-j)

        return ans


# TC: O(n)
# SC: O(n)

class Solution2:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        postsum = [0] * (10 ** 5 + 1)
        for i in range(m):
            postsum[potions[i]] += 1

        for i in range(10 ** 5 - 1, -1, -1):
            postsum[i] += postsum[i + 1]

        ans = []

        for i in range(n):
            val = success // spells[i]
            if success % spells[i] > 0: val += 1
            if val <= 10 ** 5:
                ans.append(postsum[val])
            else:
                ans.append(0)

        return ans
