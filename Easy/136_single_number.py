class Solution:
    def single_number(self, nums: list[int]):

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key,value in freq.items():
            if value == 1:
                return key

sol = Solution()
nums = [4,1,2,1,2,4,3]
result = sol.single_number(nums)
print(result)