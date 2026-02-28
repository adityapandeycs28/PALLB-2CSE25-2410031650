def row_with_max_ones(arr):
    if not arr or not arr[0]:
        return -1
    
    n = len(arr)
    m = len(arr[0])
    
    max_row_index = -1
    j = m - 1   # Start from top-right corner
    
    for i in range(n):
        while j >= 0 and arr[i][j] == 1:
            j -= 1
            max_row_index = i
    
    return max_row_index


# Example 1
arr1 = [[0,1,1,1], 
        [0,0,1,1], 
        [1,1,1,1], 
        [0,0,0,0]]

print("Output:", row_with_max_ones(arr1))


# Example 2
arr2 = [[0,0], 
        [1,1]]

print("Output:", row_with_max_ones(arr2))


# Example 3
arr3 = [[0,0], 
        [0,0]]

print("Output:", row_with_max_ones(arr3))