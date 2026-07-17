class Solution:
    def find_gcd(self, num1, num2):

        gcd = 1

        for i in range(1, min(num1, num2)+1):
            if num1 % i == 0 and num2 % i == 0:

                gcd = i

        return gcd

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

sol = Solution()
result = sol.find_gcd(num1, num2)

print(f"GCD of {num1} and {num2} is {result}")