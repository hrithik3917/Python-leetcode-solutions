class Solution:
    def upper_side(self, n):
        
        for i in range(n):
            space= 2*(n-i-1)
            
            for j in range(i+1):
                print("*", end="")

            for j in range(space):
                print(" ", end="")
            
            for j in range(i+1):
                print("*", end="")
            
            print()


    def lower_side(self, n):
        for i in range(n-1):

            for j in range(n-i-1):         #Star
                print("*", end="")
            
            for j in range(2*(i+1)):       #Space
                print(" ", end="")

            for j in range(n-i-1):         #Star
                print("*", end="")
            
            print()



sol = Solution()
n = 5
sol.upper_side(n)
sol.lower_side(n)