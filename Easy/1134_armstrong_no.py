"""
Question: The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N. 
Given a positive integer N, return true if and only if it is an Armstrong number. 
Example 1: Input: 153 Output: true Explanation: 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3. 
Example 2: Input: 123 Output: false Explanation: 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
"""

class Solution:
    def isArmstrong(self, num):
        original = num
        # count the digits
        digits = 0
        temp = num

        while temp > 0:
            digits += 1
            temp = temp // 10

        # Calculate the armstrong
        total = 0 
        temp = num 

        while temp > 0:
            last_digit = temp % 10
            temp = temp // 10

            total = total + last_digit **digits

        return total == original    
    
sol = Solution()
num = 371
result = sol.isArmstrong(num)
print(result)



"""
String Solution:
class Solution:
    def isArmstrong(self, num: int) -> bool:
        digits = str(num)
        power = len(digits)

        total = 0

        for digit in digits:
            total += int(digit) ** power

        return total == num
"""