n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ones_in_row = [0] * n
ones_in_col = [0] * m

# Compute ones count for rows and columns
for i in range(n):
    for j in range(m):
        ones_in_row[i] += arr[i][j]
        ones_in_col[j] += arr[i][j]

ans = n * m

# Calculate for rows
for i in range(n):
    ones = ones_in_row[i]
    zeros = m - ones
    ans += pow(2, ones) - ones - 1
    ans += pow(2, zeros) - zeros - 1

# Calculate for columns
for j in range(m):
    ones = ones_in_col[j]
    zeros = n - ones
    ans += pow(2, ones) - ones - 1
    ans += pow(2, zeros) - zeros - 1

print(ans)

