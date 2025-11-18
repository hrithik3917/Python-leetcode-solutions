class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [w[::-1] for w in words]
        return " ".join(reversed_words)
    
s = "Let's take LeetCode contest"
result = Solution().reverseWords(s)
print(result)
