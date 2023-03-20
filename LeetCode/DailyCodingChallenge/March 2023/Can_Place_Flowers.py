# 605. Can Place Flowers
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        if n == 0:
            return True
        for i in range(m):
            if  i == 0 and i == m-1 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == 0 and flowerbed[i] == 0 and i+1 < m and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == m-1 and flowerbed[i] == 0 and i-1 >= 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i-1 >= 0 and i+1 < m and flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0: return True

        return n == 0


# Optimized
class OptimizedSolution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        if n == 0:
            return True

        for i in range(m):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == m-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                if n == 0:
                    return True
        return n == 0
