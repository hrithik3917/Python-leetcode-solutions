class Solution:
    def pattern18(self, n):
        for i in range(n):

            #ch = ord('E')

            for j in range(ord('A')+n-i-1, ord('A')+n):
                print(chr(j), end="")
            
            print()

sol = Solution()
n = 5
sol.pattern18(n)