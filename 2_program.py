def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return [min_val, max_val]

# Example usage
arr = [1, 4, 3, 5, 8, 6]
print(find_min_max(arr))
