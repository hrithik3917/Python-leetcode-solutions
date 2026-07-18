class Solution:
    def print_name(self, name, count, num):
        if count == num:
            return
        
        print(name)

        self.print_name(name, count+1, num)

sol = Solution()
num = 5
name = 'Hritik'
sol.print_name(name, 0 , num)