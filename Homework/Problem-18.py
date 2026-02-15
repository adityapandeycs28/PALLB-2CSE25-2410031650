def is_subset(a, b):
    a.sort()
    b.sort()
    
    i = j = 0
    n, m = len(a), len(b)
    
    while i < n and j < m:
        if a[i] < b[j]:
            i += 1
        elif a[i] == b[j]:
            i += 1
            j += 1
        else:
            return False
    
    return j == m