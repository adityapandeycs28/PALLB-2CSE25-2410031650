def min_chocolate_difference(arr, m):
    n = len(arr)

    if m == 0 or n == 0 or m > n:
        return -1

    arr.sort()
    min_diff = float('inf')

    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff


# Taking input from user
arr = list(map(int, input("Enter chocolate packets separated by space: ").split()))
m = int(input("Enter number of students: "))

result = min_chocolate_difference(arr, m)

print("Minimum difference is:", result)