def smallest_subarray_length(x, arr):
    n = len(arr)
    min_length = n + 1
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        # Shrink the window while sum is greater than x
        while curr_sum > x:
            min_length = min(min_length, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    if min_length == n + 1:
        return 0
    return min_length


# Example 1
x1 = 51
arr1 = [1, 4, 45, 6, 0, 19]
print("Output:", smallest_subarray_length(x1, arr1))

# Example 2
x2 = 100
arr2 = [1, 10, 5, 2, 7]
print("Output:", smallest_subarray_length(x2, arr2))