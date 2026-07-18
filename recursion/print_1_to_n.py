class Solution:
    def print_num(self, count, num):
        if count > num:
            return
        
        print(count, end=" ")

        self.print_num(count+1, num)

sol = Solution()
num = 5
sol.print_num(1, num)