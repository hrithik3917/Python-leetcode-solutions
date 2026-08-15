class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:    # Handles the special case we are the last element
                count += 1

            if count > 1:
                return False

        return True    

sol = Solution()
nums = list(map(int, input("Enter your numbers: ").split()))
result = sol.check(nums)
print(result)