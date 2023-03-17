# 912. Sort an Array


class Solution:
    def merge(self, start, mid, end, nums):
        l = start
        h = mid + 1
        arr = []

        while l <= mid and h <= end:
            if nums[l] <= nums[h]:
                arr.append(nums[l])
                l += 1
            else:
                arr.append(nums[h])
                h += 1

        while l <= mid:
            arr.append(nums[l])
            l += 1

        while h <= end:
            arr.append(nums[h])
            h += 1

        k = end
        while k >= start:
            nums[k] = arr.pop()
            k -= 1

    def mergeSort(self, start, end, nums):
        if start < end:
            mid = (start + end) >> 1
            self.mergeSort(start, mid, nums)
            self.mergeSort(mid + 1, end, nums)
            self.merge(start, mid, end, nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergeSort(0, n - 1, nums)
        return nums