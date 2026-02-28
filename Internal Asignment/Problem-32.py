def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])  # reuse same element
            current.pop()  # backtrack
    
    backtrack(0, [], 0)
    return result


# Example 1
print("Output:", combination_sum([2,3,6,7], 7))

# Example 2
print("Output:", combination_sum([2,3,5], 8))

# Example 3
print("Output:", combination_sum([2], 1))