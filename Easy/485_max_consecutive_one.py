class Solution:
    def max_consecutive(self, nums: list[int]):

        n = len(nums)
        count = 0
        max_count = 0
        for i in range(0, n):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max(max_count, count)  # When we reach the end of the array and if we dont have the zero, then we again take max of both

sol = Solution()
nums = nums = [1,1,0,1,1,1,1,0,1,1,1,1,1,1]
result =  sol.max_consecutive(nums)
print(result)