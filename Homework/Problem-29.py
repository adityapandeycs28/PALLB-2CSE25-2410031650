import bisect

def matrix_median(mat):
    n = len(mat)
    m = len(mat[0])
    
    # Find minimum and maximum element
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)
    
    desired = (n * m) // 2
    
    while low < high:
        mid = (low + high) // 2
        
        # Count elements <= mid
        count = 0
        for row in mat:
            count += bisect.bisect_right(row, mid)
        
        if count <= desired:
            low = mid + 1
        else:
            high = mid
            
    return low


# Example 1
mat1 = [[1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]]

print("Output:", matrix_median(mat1))


# Example 2
mat2 = [[2, 4, 9],
        [3, 6, 7],
        [4, 7, 10]]

print("Output:", matrix_median(mat2))


# Example 3
mat3 = [[3],
        [4],
        [8]]

print("Output:", matrix_median(mat3))