"""
Approach: Two Pointer technique in sorted array
"""
class Solution:
    def remove(self, nums: list[int]):
        n = len(nums)
        if n == 0:
            return 0

        slow = 0
        for fast in range(1, n):
            if nums[fast] > nums[slow]:    # or we can use if nums[fast] != nums[slow]
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

sol = Solution()
nums = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5]
result = sol.remove(nums)
print(result)