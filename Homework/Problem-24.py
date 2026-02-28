def min_swaps(arr, k):
    n = len(arr)

    # Step 1: Count elements <= k
    good = 0
    for num in arr:
        if num <= k:
            good += 1

    # Step 2: Count bad elements in first window
    bad = 0
    for i in range(good):
        if arr[i] > k:
            bad += 1

    ans = bad

    # Step 3: Slide the window
    i = 0
    j = good
    while j < n:
        # Remove left element
        if arr[i] > k:
            bad -= 1

        # Add right element
        if arr[j] > k:
            bad += 1

        ans = min(ans, bad)

        i += 1
        j += 1

    return ans


# Example 1
arr1 = [2, 1, 5, 6, 3]
k1 = 3
print("Output:", min_swaps(arr1, k1))

# Example 2
arr2 = [2, 7, 9, 5, 8, 7, 4]
k2 = 6
print("Output:", min_swaps(arr2, k2))

# Example 3
arr3 = [2, 4, 5, 3, 6, 1, 8]
k3 = 6
print("Output:", min_swaps(arr3, k3))