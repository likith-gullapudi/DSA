# Dictionary with valid moves
d = {'RS': 1, 'SP': 1, 'PR': 1}

# List of possible moves
moves = ['P', 'R', 'S']


# Recursive function with memoization
def rec(index, used, prev):
    if used == k + 2:
        return -float('inf')
    if index == len(arr):
        return 0
    # Check if the state has been computed already
    if dp[index][used][prev_map[prev]] != -1:
        return dp[index][used][prev_map[prev]]

    # Base cases

    ans = -1
    for move in moves:
        current_score = d.get(move + arr[index], 0) + rec(index + 1, used + int(move != prev), move)
        if current_score > ans:
            ans = current_score
            move_choice[index][used][prev_map[prev]] = move

    # Store the computed value in the memoization table
    dp[index][used][prev_map[prev]] = ans
    return ans


# Function to print the solution path
def printsol(index, used, prev):
    path = []
    while index < len(arr):
        move = move_choice[index][used][prev_map[prev]]
        if not move:
            break
        path.append(move)
        used += int(move != prev)
        prev = move
        index += 1
    return path


# Main function
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    arr = [x for x in input()]

    # Initialize memoization table with -1
    dp = [[[-1 for _ in range(4)] for _ in range(k + 3)] for _ in range(n + 1)]

    # Initialize move choice table
    move_choice = [[['' for _ in range(4)] for _ in range(k + 3)] for _ in range(n + 1)]

    # Mapping of moves to indices for memoization
    prev_map = {'R': 0, 'P': 1, 'S': 2, 'a': 3}

    # Compute the maximum score
    max_score = rec(0, 0, 'a')

    # Print the maximum score
    print(max_score)

    # Print the solution path
    path = printsol(0, 0, 'a')
    print(''.join(path))
