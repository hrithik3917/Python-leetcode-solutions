class Solution:
    def pattern11(self, n):
        for i in range(n):
            # If the row index is even, start with 1
            if i % 2 == 0:
                start = 1
            else:
                start = 0

            # Loop to print alternating 1's and 0's
            for j in range(i+1):
                print(start, end="")
                # Alternate between 1 and 0
                start = 1-start
            
            print()

sol = Solution()
n = 5
sol.pattern11(n)
