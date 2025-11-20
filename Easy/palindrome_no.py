class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
    
x = 121
result = Solution().isPalindrome(x)
print(result)


"""
Other approaches to solve the problem include:
1. Two pointer technique: Compare characters from the start and end of the string moving towards the center.
2. Mathematical approach: Reverse the integer mathematically without converting it to a string and compare with the original integer.

1. Two pointer technique:
 class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        s = str(x)              # convert number to string
        left, right = 0, len(s) - 1

        # move pointers towards the center
        while left < right:
            if s[left] != s[right]:
                return False    # mismatch → not palindrome
            left += 1
            right -= 1

        # if we didn't find mismatch, it's a palindrome
        return True

2. Mathematical approach:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        # build the reversed number
        while x != 0:
            digit = x % 10              # get last digit
            reversed_num = reversed_num * 10 + digit
            x //= 10                    # remove last digit
        
        return original == reversed_num

"""