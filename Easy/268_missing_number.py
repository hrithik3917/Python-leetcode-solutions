class Solution:
    def missing_number(self, nums: list[int]):

        n = len(nums)
        freq = {}

        for i in range(0, n+1):
            freq[i] = 0

        for num in nums:
            freq[num] = 1

        for key, value in freq.items():
            if value == 0:
                 return key

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing_number(nums)
print(result)





#--------- Optimal Solution ----------

class Solution:
    def missing(self, nums):
        n = len(nums)
        return (n * (n+1) // 2) - sum(nums)

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing(nums)
print(result)
