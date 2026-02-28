def is_palindrome(num):
    # Convert number to string and compare with its reverse
    return str(num) == str(num)[::-1]


def all_palindrome(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


# Example 1
arr1 = [111, 222, 333, 444, 555]
print("Output:", all_palindrome(arr1))

# Example 2
arr2 = [121, 131, 20]
print("Output:", all_palindrome(arr2))