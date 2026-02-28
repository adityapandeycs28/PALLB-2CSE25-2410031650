def three_way_partition(arr, a, b):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif a <= arr[mid] <= b:
            mid += 1

        else:  # arr[mid] > b
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return True   # If partition successful


# Example 1
arr1 = [1, 2, 3, 3, 4]
a1, b1 = 1, 2
result1 = three_way_partition(arr1, a1, b1)
print("Modified Array:", arr1)
print("Output:", result1)

# Example 2
arr2 = [1, 4, 3, 6, 2, 1]
a2, b2 = 1, 3
result2 = three_way_partition(arr2, a2, b2)
print("Modified Array:", arr2)
print("Output:", result2)