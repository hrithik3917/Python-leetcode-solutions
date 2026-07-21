class Solution:
    def fibonacci(self, num):
        if num <= 1:
            return num
        
        return self.fibonacci(num-1) + self.fibonacci(num-2)
    
sol = Solution()
num = int(input("Enter Number:"))
result = sol.fibonacci(num)
print(result)
