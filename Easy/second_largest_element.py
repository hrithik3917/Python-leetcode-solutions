class Solution:
    def second_smallest_and_largest(self, nums):

        if len(nums) < 2:
            return -1, -1

        else:
            smallest = float('inf')
            second_smallest = float('inf')
            largest = float('-inf')
            second_largest = float('-inf')

            for num in nums:
                if num < smallest:
                    second_smallest = smallest
                    smallest = num

                elif num < second_smallest and num != smallest:
                    second_smallest = num 

                if num > largest:
                    second_largest = largest
                    largest = num

                elif num > second_largest and num != largest:
                    second_largest = num

            if second_smallest == float('inf'):
                second_smallest = -1

            if second_largest == float('-inf'):
                second_largest = -1

            return second_smallest, second_largest

sol = Solution()
nums = [1,9,3,4,7,7,5]
result =  sol.second_smallest_and_largest(nums)
print(result)
