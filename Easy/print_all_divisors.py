class Solution:
    def getDivisors(self, num: int) -> list[int]:
        divisors = []

        i = 1

        while i*i < num:
            if num % i == 0:
                divisors.append(i)
                other_divisor = num // i

                if other_divisor != i:
                    divisors.append(other_divisor)

            i += 1
        
        divisors.sort()
        return divisors

sol = Solution()
num = 36
result = sol.getDivisors(num)
print(result)
            

