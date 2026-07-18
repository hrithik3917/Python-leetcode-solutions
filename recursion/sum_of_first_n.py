"""
This is called tail recursion.
It carry the total into the next call"""

class Solution:
    def sum_of_natural_numbers(self, count, num, total=0):

        if count > num:
            return total
        
        total = total + count

        return self.sum_of_natural_numbers(count+1, num, total)

sol = Solution()
num = int(input("Enter your number: "))
result = sol.sum_of_natural_numbers(1, num)
print(result)



# Second approach (Most preferred):
class Solution:
    def sum_of_natural_numbers(self, num):
        if num == 0:
            return 0
        
        return num + self.sum_of_natural_numbers(num-1)
    
sol = Solution()
num = int(input("Enter Number: "))
print(sol.sum_of_natural_numbers(num))



        
        
        
