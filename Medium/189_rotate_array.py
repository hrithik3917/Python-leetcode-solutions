class Solution:
    def rotate_array(self, nums: list[int], k: int):
        n = len(nums)
        k %= n  #This handles cases where k >= n

        nums[:] = nums[n-k:] + nums[:n-k]
        return nums

sol = Solution()
nums = [3,9,5,2,6,7,8,1]
k = int(input("Enter value of K: "))
result = sol.rotate_array(nums, k)
print(result)


# -----------Reversal Method-----------------
class Solution:
    def rotate_array(self, nums: list[int], k: int):
        n = len(nums)
        k %= n

        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # 1. Reverse the entire array
        reverse(0, n-1)
        # 2. Reverse the first k elements
        reverse(0, k-1)
        # 3. Reverse the rest of the array
        reverse(k, n-1)

        return nums

sol = Solution()
nums = [3,9,5,2,6,7,8,1]
k = int(input("Enter value of K: "))
result = sol.rotate_array(nums, k)
print(result)


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""