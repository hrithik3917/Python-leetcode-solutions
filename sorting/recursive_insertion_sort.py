class Solution:
    def recursive_insertion_sort(self, arr: list[int], n: int):
        # Base case: 0 or 1 elements are already sorted
        if n <= 1:
            return


        self.recursive_insertion_sort(arr, n-1)

        self._insertLast(arr, n-1)


    def _insertLast(self, arr: list[int], i: int):
        # Base case: reached the start, or left element is already <= its right element
        if i == 0 or arr[i-1] <= arr[i]:
            return

        arr[i], arr[i-1] = arr[i-1], arr[i]

        # Continue moving left
        self._insertLast(arr, i-1)

sol= Solution()
arr = list(map(int, input("Enter your array: ").split()))
n = len(arr)
sol.recursive_insertion_sort(arr, n)
print(arr)