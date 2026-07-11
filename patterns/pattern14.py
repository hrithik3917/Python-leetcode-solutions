class Solution:
    def pattern14(self, n):
        for i in range(n):
            # Inner loop to print alphabets from A to A + i
            for j in range(i+1):
                print(chr(65+j), end=" ")       # Print the alphabet character followed by a space
            
            print()

sol = Solution()
n = 5
sol.pattern14(n)