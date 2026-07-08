class Solution:
    def pattern1(self, n):
        for i in range (n):
            for j in range(n):
             
             print("*", end=" ")
            # After printing stars in a row, move to the next line
            print()


sol = Solution()
n = 5
sol.pattern1(n)