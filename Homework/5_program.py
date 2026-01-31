def largest_element(arr):
    max_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num

    return max_val

# Example usage
arr = [1, 8, 7, 56, 90]
print(largest_element(arr))
