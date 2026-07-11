class Solution:
    def pattern13(self, n):
        num = 0
        for i in range(n):

            for j in range(i+1):
                print(num + 1, end=" ")
                num = num + 1
            print()
        
sol = Solution()
n = 5
sol.pattern13(n)