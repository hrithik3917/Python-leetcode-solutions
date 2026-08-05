# Asceding order selection sort

class Solution:
    def selection_sort(self, nums):
        n = len(nums)

        for i in range(0, n):
            min_index = i

            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i], nums[min_index] = nums[min_index],nums[i]

        return nums


sol = Solution()
nums = [7, 9, 6, 2, 1, 5, 4]
result = sol.selection_sort(nums)
print(result)




# Descending order selection sort

class Solution:
    def selection_sort(self, nums):
        n = len(nums)

        for i in range(0, n):
            max_index = i

            for j in range(i+1, n):
                if nums[j] > nums[max_index]:
                    max_index = j

            nums[i], nums[max_index] = nums[max_index],nums[i]

        return nums


sol = Solution()
nums = [7, 9, 6, 2, 1, 5, 4]
result = sol.selection_sort(nums)
print(result)