class Solution:
    def recursive_bubble_sort(self, arr: list[int], n: int):

        if n == 1:
            return

        self._oneSweep(arr, n, 0)

        self.recursive_bubble_sort(arr, n-1)


    def _oneSweep(self, arr:list[int], n: int, i: int):

        if i == n-1:
            return

        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

        self._oneSweep(arr, n, i+1)

sol = Solution()
arr = list(map(int, input("Enter your array: ").split()))
n = len(arr)
sol.recursive_bubble_sort(arr, n)
print(arr)