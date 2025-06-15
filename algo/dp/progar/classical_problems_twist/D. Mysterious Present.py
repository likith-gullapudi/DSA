import sys
sys.setrecursionlimit(10**4)

# Input and preprocessing
n, w, h = [int(x) for x in input().split()]
cards = []
for _ in range(n):
    x = [int(x) for x in input().split()]
    if x[0] <= w or x[1] <= h:
        continue
    cards.append(x + [_ + 1])
cards.sort()
cards = [(w, h, 0)] + cards
n = len(cards)

# Space optimization using rolling arrays
next_row = [0] * (n + 1)  # Represent dp[index + 1]
current_row = [0] * (n + 1)  # Represent dp[index]

for index in range(n - 1, 0, -1):
    for prev_index in range(index, -1, -1):
        a = b = 0
        if cards[index][0] > cards[prev_index][0] and cards[index][1] > cards[prev_index][1]:
            a = 1 + next_row[index]  # Taking the current card
        b = next_row[prev_index]  # Not taking the current card
        current_row[prev_index] = max(a, b)
    next_row, current_row = current_row, next_row  # Swap rows

# Extract the result from the space-optimized dp array
ans = next_row[0]
print(ans)

# Print solution path
def printsol_iterative(dp_row):
    index, prev_index = 1, 0  # Start from the first card with no previous card
    solution = []  # To store the selected cards

    while index < n:  # Process all cards
        a = b = 0
        if cards[index][0] > cards[prev_index][0] and cards[index][1] > cards[prev_index][1]:
            a = 1 + dp_row[index]  # Value if we take the current card
        b = dp_row[prev_index]  # Value if we don't take the current card

        # Check if taking the current card is part of the optimal solution
        if a >= b and a != 0:
            solution.append(cards[index][2])  # Add card's original index to the solution
            prev_index = index  # Update prev_index to the current card
        # Move to the next card
        index += 1

    print(" ".join(map(str, solution)))  # Print the solution in order


if ans != 0:
    printsol_iterative( current_row)
