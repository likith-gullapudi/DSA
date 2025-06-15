import bisect

# Example list
arr = [1, 2, 4, 4, 4, 5, 6, 7]

# Element to insert/find
x = 0

# Using bisect_left
# Finds the first position where 4 can be inserted to maintain sorted order
left_index = bisect.bisect_left(arr, x)
print(f"bisect_left: Position to insert {x} to keep sorted order is {left_index}")

# Using bisect_right
# Finds the last position where 4 can be inserted to maintain sorted order
right_index = bisect.bisect_right(arr, x)
print(f"bisect_right: Position to insert {x} to keep sorted order is {right_index}")

# Show the positions and the modified lists
print(f"Array: {arr}")
print(f"Array with {x} inserted at bisect_left position: {arr[:left_index] + [x] + arr[left_index:]}")
print(f"Array with {x} inserted at bisect_right position: {arr[:right_index] + [x] + arr[right_index:]}")
