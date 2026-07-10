class Solution:
    def pattern8(self, n):
        for i in range(n):

            for j in range(i):
                print(" ", end="")   # Space 

            for j in range(2*n-(2*i+1)):     # Star:- Formula = 2n-(2i+1) 
                print("*", end="")

            for j in range(i):
                print(" ", end="")     # Space

            print()

sol = Solution()
n = 5
sol.pattern8(n)