class Solution:
    def is_palindrome(self, i, str):

        if i >= len(str)//2:
            return True
        
        if str[i] != str[len(str)-i-1]:
            return False
        
        return self.is_palindrome(i+1, str)
    

sol = Solution()
str = input("Enter a string: ")
result = sol.is_palindrome(0, str)
print(result)