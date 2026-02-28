def search_insert(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low   # Insert position


# Example 1
nums1 = [1,3,5,6]
print("Output:", search_insert(nums1, 5))

# Example 2
nums2 = [1,3,5,6]
print("Output:", search_insert(nums2, 2))

# Example 3
nums3 = [1,3,5,6]
print("Output:", search_insert(nums3, 7))