class Solution:
    def count_frequency(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return freq

sol = Solution()
nums = [10, 5, 10, 5, 34, 7, 98, 7, 34]
result = sol.count_frequency(nums)
print(result)