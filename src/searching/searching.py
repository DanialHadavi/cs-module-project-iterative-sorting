def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr)
    while True:
        mid = round((low + high) / 2)
        if high < low or mid >= len(arr):
            return -1  # not found
        current = arr[mid]
        if target == current:
            return mid
        elif target < current:
            high = mid
        else:
            low = mid + 1
