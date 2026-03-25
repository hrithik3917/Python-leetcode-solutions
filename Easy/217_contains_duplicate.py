"""To solve this question we have many methods
1. Sorting: 
If we sort the array, then any duplicate values will appear next to each other.
Sorting groups identical elements together, so we can simply check adjacent positions to detect duplicates.
This reduces the problem to a single linear scan after sorting, making it easy to identify if any value repeats."""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
    
nums = [1, 2, 3, 3]
result = Solution.hasDuplicate(nums)
print(result)
    
"""
Follwoing are the more approaches:

2. Brute Force:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if num[i] == num[j]:
                    return True

        return False



3. Hash Set: 
We can use a hash set to efficiently keep track of the values we have already encountered.
As we iterate through the array, we check whether the current value is already present in the set.
If it is, that means we've seen this value before, so a duplicate exists.
Using a hash set allows constant-time lookups, making this approach much more efficient than comparing every pair.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

        
4. Hash Set length:
This approach uses the same idea as the previous hash set method: a set only stores unique values, so duplicates are automatically removed.
Instead of checking each element manually, we simply compare the length of the set to the length of the original array.
If duplicates exist, the set will contain fewer elements.
The logic is identical to the earlier approach — this version is just a shorter and more concise implementation of it.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    """

