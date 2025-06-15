from bisect import bisect_left

# Sample sorted array
arr = [1, 3, 5, 7, 8, 10, 12]

# Target element
target = 9

# Find position using bisect_left
idx = bisect_left(arr, target)

# Check if we need the exact element or just before
if idx < len(arr) and arr[idx] == target:
    result = arr[idx]  # Element found
elif idx > 0:
    result = arr[idx - 1]  # Element just before 9
else:
    result = None  # No valid element (9 is less than all elements)

print(result)
