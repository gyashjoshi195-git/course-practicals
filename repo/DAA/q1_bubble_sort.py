"""Q1: Bubble Sort - steps and time complexity.

Steps:
1. Compare each pair of adjacent elements.
2. If left > right, swap them.
3. After each pass the largest unsorted element "bubbles" to the end.
4. Repeat for n-1 passes (stop early if a pass makes no swaps).

Time complexity:
  Worst case   : O(n^2)  (array in reverse order)
  Average case : O(n^2)
  Best case    : O(n)    (already sorted, thanks to the 'swapped' flag)
Space        : O(1)
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Pass {i + 1}: {arr}")
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    print("Sorted  :", bubble_sort(data))
