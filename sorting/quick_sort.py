class Solution:
    def quick_sort(self, nums: list[int], low: int, high: int):
        if low >= high:
            return

        pIndex = self._partition(nums, low, high)

        self.quick_sort(nums, low, pIndex - 1)
        self.quick_sort(nums, pIndex + 1, high)


    def _partition(self, nums: list[int], low: int, high: int):
        pivot = nums[low]
        i = low
        j = high

        while i < j:
            while nums[i] <= pivot and i <= high-1:
                i += 1

            while nums[j] > pivot and j >= low + 1:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        #Place the pivot in the correct sorted position
        nums[j], nums[low] = nums[low], nums[j]
        return j

sol = Solution()
nums = [4, 1, 7, 6, 3, 2, 8]
n = len(nums)
sol.quick_sort(nums, 0, n-1)
print(nums)