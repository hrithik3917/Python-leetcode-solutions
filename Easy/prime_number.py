"""
Check if a number is prime or not.
Problem Statement: Given an integer N, check whether it is prime or not. 
A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2..
"""
# Brute Force Approach
class Solution:
    def isPrime(self, num: int) -> bool:
        
        count = 0

        for i in range(1, num+1):
            if num % i == 0:
                count += 1
            
        return count == 2
    
sol = Solution()
num = 23
result = sol.isPrime(num)

if result:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")