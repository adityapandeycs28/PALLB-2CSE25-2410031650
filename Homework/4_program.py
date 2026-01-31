def union_arrays(a, b):
    return list(set(a) | set(b))

# Example usage
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(union_arrays(a, b)))
