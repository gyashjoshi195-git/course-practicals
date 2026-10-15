"""Q2: Merge Sort using Divide and Conquer.

Divide  : split the array into two halves.
Conquer : recursively sort each half.
Combine : merge the two sorted halves into one sorted array.

Recurrence: T(n) = 2T(n/2) + O(n)  ->  O(n log n) in all cases.
Space: O(n)
"""


def merge_sort(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}Divide: {arr}")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)
    merged = merge(left, right)
    print(f"{indent}Merge : {left} + {right} -> {merged}")
    return merged


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted:", merge_sort(data))
