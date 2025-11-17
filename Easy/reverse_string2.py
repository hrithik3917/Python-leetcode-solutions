"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
 
Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        
        for i in range(0, len(s), 2*k):

            first_k = s[i:i+k][::-1]
            next_k = s[i+k:i+2*k]

            result.append(first_k + next_k)

        return "".join(result)

s = "hritiksangramdalavi"
k = 2
result = Solution().reverseStr(s, k)
print(result)

