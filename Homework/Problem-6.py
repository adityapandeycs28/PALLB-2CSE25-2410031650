def rotate_by_one(arr):
    n = len(arr)
    if n == 0:
        return arr
    
    last = arr[-1]
    
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = last
    return arr


arr = [1, 2, 3, 4, 5]
print(rotate_by_one(arr))   
