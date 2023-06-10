# 1802. Maximum Value at a Given Index in a Bounded Array
# Leetcode Medium
# Date: 10 June 2023
# TC: O(log(N))
# SC: O(1)


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, h = 1, maxSum
        ans = 1
        lft, rht = index, n - index - 1

        while l <= h:
            mid = (l + h) >> 1
            summ = mid + n - 1
            j = mid - 2

            if j != 0:
                if j <= lft:
                    summ += (j ** 2 + j) // 2
                elif lft != 0:
                    summ += (j ** 2 + j) // 2 - (abs(lft - j) ** 2 + abs(lft - j)) // 2

                if j <= rht:
                    summ += (j ** 2 + j) // 2
                elif rht != 0:
                    summ += (j ** 2 + j) // 2 - (abs(rht - j) ** 2 + abs(rht - j)) // 2

            if summ <= maxSum:
                ans = max(ans, mid)
                l = mid + 1
            else:
                h = mid - 1

        return ans
