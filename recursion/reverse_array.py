class Solution:
    def reverse_array(self, arr, left, right):

        if left >= right:
            return
        
        arr[left], arr[right] = arr[right], arr[left]

        self.reverse_array(arr, left+1, right-1)

sol = Solution()
arr = list(map(int, input("Enter number: ").split()))
sol.reverse_array(arr, 0, len(arr)-1)
print("Reversed array:", arr)

