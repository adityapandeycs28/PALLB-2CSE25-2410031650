def find_median(arr):
    arr.sort()  # Step 1: Sort the array
    n = len(arr)

    if n % 2 == 1:
        # Odd number of elements
        return arr[n // 2]
    else:
        # Even number of elements
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# Example 1
arr1 = [90, 100, 78, 89, 67]
print("Output:", find_median(arr1))

# Example 2
arr2 = [56, 67, 30, 79]
print("Output:", find_median(arr2))

# Example 3
arr3 = [1, 2]
print("Output:", find_median(arr3))