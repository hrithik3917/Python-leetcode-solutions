class Solution:
    def pattern12(self, n):
        spaces = 2*(n-1)

        # Outer loop for the number of rows
        for i in range(1, n+1):

            # Inner loop to print numbers in increasing order
            for j in range(1, i+1):
                print(j, end="")

            # Inner loop to print spaces in the middle
            for j in range(1, spaces+1):
                print(" ", end="")
                
            # Inner loop to print numbers in decreasing order
            for j in range(i, 0, -1):
                print(j, end="")

            print()
            
            spaces -= 2         # Decrease spaces by 2 after each row

sol = Solution()
n =5
sol.pattern12(n)