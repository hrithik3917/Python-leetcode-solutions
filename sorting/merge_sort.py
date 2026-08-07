class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)
        return self.merge_array(left_sorted, right_sorted)




    def merge_array(self, left, right):

        result = []
        i,j = 0, 0
        n = len(left)
        m = len(right)

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i < n:
            while i < n:
                result.append(left[i])
                i += 1

        if j < m:
            while j < m:
                result.append(right[j])
                j += 1

        return result


sol = Solution()
nums = [3,1,6,2,4,8,7]
result = sol.merge_sort(nums)
print(result)





# Instead of using the if and while loop in the merge_array function we can also use the Slicing

class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)
        
        return self.merge_array(left_sorted, right_sorted)

    def merge_array(self, left, right):
        result = []
        i = j = 0
        n, m = len(left), len(right)

        # Merge elements in sorted order
        while i < n and j < m:
            if left[i] <= right[j]: 
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append remaining elements using slicing
        result.extend(left[i:])
        result.extend(right[j:])

        return result