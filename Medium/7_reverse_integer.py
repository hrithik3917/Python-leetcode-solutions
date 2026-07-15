class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN = -(2**31)
        INT_MAX = 2**31-1

        if x < 0:
            sign = -1
        else: 
            sign = 1
        
        x = abs(x)

        reversed_num = 0

        while x > 0:
            last_digit = x % 10
            x = x//10

            if reversed_num > (INT_MAX - last_digit) // 10:
                return 0
            
            reversed_num = reversed_num*10 + last_digit

        return sign*reversed_num

sol = Solution()
x = -566
result = sol.reverse(x)
print(result)