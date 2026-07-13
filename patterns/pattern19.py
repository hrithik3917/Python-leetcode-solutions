class Solution:
    def upper_part(self, n):
        for i in range(n):

            for j in range(n-i):
                print("*", end="")
            
            for j in range(2*i+1):
                print(" ", end="")
            
            for j in range(n-i):
                print("*", end="")
            
            print()

    def lower_part(self, n):
        space = 2*n-2

        for i in range(n):

            for j in range(i+1):
                print("*", end="")

            for j in range(space+1):
                print(" ", end="")
            
            for j in range(i+1):
                print("*", end="")
            
            space -= 2 
            
            print()


sol = Solution()
n=5
sol.upper_part(n) 
sol.lower_part(n)            