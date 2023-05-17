# 2215. Find the Difference of Two Arrays
# Leetcode Easy
# Date: 2 May 2023
# TC: O(N)
# SC: O(1)
from typing import List


class Solution:

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1, arr2 = [], []
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0

        while i < n and j < m:
            if nums1[i] == nums2[j]:
                val = nums2[j]
                while i < n and nums1[i] == val:
                    i += 1
                while j < m and nums2[j] == val:
                    j += 1
            elif nums1[i] < nums2[j]:
                arr1.append(nums1[i])
                val = nums1[i]
                while i < n and nums1[i] == val:
                    i += 1
            else:
                arr2.append(nums2[j])
                val = nums2[j]
                while j < m and nums2[j] == val:
                    j += 1
        while i < n:
            arr1.append(nums1[i])
            val = nums1[i]
            while i < n and nums1[i] == val:
                i += 1

        while j < m:
            arr2.append(nums2[j])
            val = nums2[j]
            while j < m and nums2[j] == val:
                j += 1

        return [arr1, arr2]
