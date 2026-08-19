class Solution:
    def rotate_array(self, nums: list[int]):
        n = len(nums)

        if n <= 1:
            return 0

        temp = nums[n-1]

        for i in range(n-2, -1, -1):
            nums[i+1] = nums[i]

        nums[0] = temp
        return nums

sol = Solution()
nums = [7,5,3,1,9,-2,1,6]
result = sol.rotate_array(nums)
print(result)



# -------We can use slicing method also----------

class Solution:
    def rotate_array(self, nums: list[int]):
        n = len(nums)

        nums[:] = [nums[-1]] + nums[ :n-1]
        return nums

sol = Solution()
nums = [7,5,3,1,9,-2,1,6]
result = sol.rotate_array(nums)
print(result)