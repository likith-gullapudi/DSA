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

for index in range(n - 1, -1, -1):
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
def printsol(index, prev_index, dp_row):
    if index == len(cards):
        return
    a = b = 0
    if cards[index][0] > cards[prev_index][0] and cards[index][1] > cards[prev_index][1]:
        a = 1 + dp_row[index]
    b = dp_row[prev_index]
    if a >= b and a != 0:
        print(cards[index][2], end=" ")
        printsol(index + 1, index, next_row if index + 1 < n else [0] * (n + 1))
    else:
        printsol(index + 1, prev_index, dp_row)

if ans != 0:
    printsol(1, 0, next_row)