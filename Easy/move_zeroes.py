class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        left  = 0
        # 1) Move all non-zero elements to the front
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        while left < len(nums):
            nums[left] = 0
            left += 1


num = [3,1,0,0,4,2]
Solution().moveZeroes(num)
print(num)
