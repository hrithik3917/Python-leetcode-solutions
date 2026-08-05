class Solution:
     def bubble_sort(self, nums):
          
        n = len(nums)
        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

sol = Solution()
nums = [5, 1, 6, 8, 2, 4, 9]
result = sol.bubble_sort(nums)
print(result)



"""
Best case scenario: If the array is already sorted then in that case we can check if the swapping is already happened
or not.
In that case, 
Time Complexity = O(N),
Space Complexity = O(1)
"""

class Solution:
     def bubble_sort(self, nums):
          
        n = len(nums)
        for i in range(n-2, -1, -1):
            is_swap = False

            for j in range(0, i+1):
                if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swap = True

            #If no two elements were swapped  in the inner loop then array is sorted
            if not is_swap:
                break

        return nums

sol = Solution()
nums = [5, 1, 6, 8, 2, 4, 9]
result = sol.bubble_sort(nums)
print(result)