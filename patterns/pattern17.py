class Solution:
    def pattern17(self, n):
        for i in range(n):
            #Space
            for j in range(n-i-1):
                print(" ", end=" ")

            #Letter 
            ch = ord('A')
            breakpoint = (2*i+1) // 2

            for j in range(1, 2*i+2):
                print(chr(ch), end=" ")
                if j <= breakpoint:
                    ch += 1
                else:
                    ch -= 1

            #Space
            for j in range(n-i-1):
                print(" ", end=" ")

            print()

sol = Solution()
n = 5
sol.pattern17(n)