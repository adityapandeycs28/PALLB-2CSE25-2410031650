def combination_sum2(candidates, target):
    candidates.sort()  # Sort to handle duplicates
    result = []

    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates at the same recursion level
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])
            backtrack(i + 1, current, total + candidates[i])  # i+1 → use once
            current.pop()

    backtrack(0, [], 0)
    return result


# Example 1
candidates1 = [10,1,2,7,6,1,5]
target1 = 8
print("Output:", combination_sum2(candidates1, target1))

# Example 2
candidates2 = [2,5,2,1,2]
target2 = 5
print("Output:", combination_sum2(candidates2, target2))