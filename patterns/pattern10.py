class Solution:
    def upper_side(self, n):
        for i in range(n):

            for j in range(i+1):
                print("*", end="")      

            print()

    def lower_side(self, n):
        for i in range(n-1):

            for j in range(n-i-1):
                print("*", end="")     
            
            print()

sol = Solution()
n = 5
sol.upper_side(n)
sol.lower_side(n)
