def min_path( row, col):
    # Base case: if we reach the bottom-right corner
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]

    # If we reach out of the grid or encounter a cell we can't go to, return infinity
    if row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
        return float('inf')

    # If the value is already memoized, return it
    if memo[row][col] != -1:
        return memo[row][col]

    # Move right and down recursively, and memoize the result
    memo[row][col] = grid[row][col] + min(min_path(grid, row, col + 1, memo), min_path(grid, row + 1, col, memo))

    return memo[row][col]


# Example usage:
grid = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# Initialize memoization table with -1
memo = [[-1] * len(grid[0]) for _ in range(len(grid))]
count= [[-1] * len(grid[0]) for _ in range(len(grid))]


def counting(i, j):
    # Base case: if we reach beyond the grid boundaries or encounter a barrier, return 0
    if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return 0

    # If we reach the bottom-right corner, return 1
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return 1

    # If the count for the current position is already calculated, return it
    if count[i][j] != -1:
        return count[i][j]

    total_paths = 0

    # Check if moving down is part of the minimum path
    total_paths += min_path(i,j)==min_path(i+1,j)-1 and  counting(i + 1, j)

    # Check if moving right is part of the minimum path
    total_paths += min_path(i,j)==min_path(i,j+1)-1 and  counting(i, j + 1)

    # Memoize the count for the current position
    count[i][j] = total_paths

    return total_paths


print("Minimum length of path:", min_path(grid, 0, 0, memo))
print(memo)
print(counting(0,0))
