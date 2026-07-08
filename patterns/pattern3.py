class Solution:
    def pattern3(self, n):
        for i in range(n):
            for j in range(i + 1):
                print(j + 1, end=" ")

            print()

sol = Solution()
n = 5
sol.pattern3(n)