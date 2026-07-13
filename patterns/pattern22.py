class Solution:
    def pattern22(self, n):

        size = 2*n-1

        for i in range(size):
            for j in range(size):

                top = i
                left = j
                bottom = size-1-i    # size=7
                right = size-1-j

                minimum_distance = min(top, left, bottom, right)

                value = n - minimum_distance

                print(value, end=" ")
            
            print()

sol = Solution()
n=4
sol.pattern22(n)