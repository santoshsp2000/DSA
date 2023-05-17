# 2336. Smallest Number in Infinite Set
# Leetcode Medium
# Date: 25 April 2023
# TC: O(N)
# SC: O(N)
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        for i in range(1, 1001):
            heapq.heappush(self.heap, i)

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        return -1

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
