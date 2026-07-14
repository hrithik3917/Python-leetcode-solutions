""" Que: Given the number 'n'. find out and return the number of digits present in a number.
Sample input: 156 
Sample Output: 3
"""

class Solution:
    def count_number(self, num):

        count = 0

        while num > 0:
            num = num // 10
            count += 1
        
        return count
    
sol = Solution()
num = 7789444
result = sol.count_number(num)
print(result)





# The below code returns the single number in reverse order

# class Solution:
#     def get_number(self, num):

#         digits = []

#         while num > 0:
#             last_digit = num % 10
#             digits.append(last_digit)   
#             num = num // 10
#         return digits

# sol = Solution()
# num = 7789
# result = sol.count_number(num)
# print(result)