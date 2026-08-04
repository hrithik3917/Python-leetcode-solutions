from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        window_sum = 0
        max_frequency = 1

        for right in range(len(nums)):
            window_sum += nums[right]

            while (
                nums[right] * (right-left+1) > window_sum + k
            ):

                window_sum -= nums[left]
                left += 1

            current_frequency = right - left + 1
            max_frequency = max(max_frequency, current_frequency)

        return max_frequency

sol = Solution()
nums = [1,2,4]

result = sol.maxFrequency(nums, 2)
print(result)

            
            