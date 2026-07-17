"""
Check if a number is prime or not.
Problem Statement: Given an integer N, check whether it is prime or not. 
A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2..
"""

class Solution:
    def checkPrime(self, num: int)->int:

        if num < 2:
            return False
        
        if num == 2:
            return True

        if num % 2 == 0:         # Any other even number is not prime
            return False
        
        i = 3                    # Check only odd possible divisors

        while i*i < num:
            if num % i == 0:
                return False
            
            i += 2

        return True
    
# Ask the user to enter a number
N = int(input("Enter a number: "))

sol = Solution()
result = sol.checkPrime(N)

if result:
    print(N, "is a prime number.")
else:
    print(N, "is not a prime number.")




# Brute Force Approach
class Solution:
    def isPrime(self, num: int) -> bool:
        
        count = 0

        for i in range(1, num+1):
            if num % i == 0:
                count += 1
            
        return count == 2
    
N = int(input("Enter a number: "))

sol = Solution()
result = sol.isPrime(N)

if result:
    print(N, "is a prime number.")
else:
    print(N, "is not a prime number.")
