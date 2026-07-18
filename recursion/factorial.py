class Solution:
    def factorial(self, num):
        if num == 1:
            return 1
        
        return num * self.factorial(num-1)
    
sol = Solution()
num = int(input("Enter number: "))
result = sol.factorial(num)
print(result)   