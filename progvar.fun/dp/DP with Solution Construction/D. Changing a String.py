s = input().strip()
t = input().strip()
n, m = len(s), len(t)

dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
path = [[None for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n, -1, -1):
    for j in range(m, -1, -1):
        if i == n and j == m:
            dp[i][j] = 0
            continue

        options = []

        # Match
        if i < n and j < m and s[i] == t[j]:
            options.append((dp[i + 1][j + 1], (i + 1, j + 1, "MATCH", s[i])))

        # Replace
        if i < n and j < m and s[i] != t[j]:
            options.append((1 + dp[i + 1][j + 1], (i + 1, j + 1, "REPLACE", (s[i], t[j]))))

        # Delete
        if i < n:
            options.append((1 + dp[i + 1][j], (i + 1, j, "DELETE", s[i])))

        # Insert
        if j < m:
            options.append((1 + dp[i][j + 1], (i, j + 1, "INSERT", t[j])))

        dp[i][j], path[i][j] = min(options, key=lambda x: x[0])

print(dp[0][0])  # minimum edits

# Trace path
ops = []
i, j = 0, 0
cur_pos = 1  # current position in "s" while applying edits
while (i, j) != (n, m):
    ni, nj, action, data = path[i][j]

    if action == "MATCH":
        i, j = ni, nj
        cur_pos += 1
        continue

    if action == "REPLACE":
        old, new = data
        ops.append(f"REPLACE {cur_pos} {new}")
        i, j = ni, nj
        cur_pos += 1

    elif action == "DELETE":
        ops.append(f"DELETE {cur_pos}")
        i, j = ni, nj
        # cur_pos stays the same, since string shrinks

    elif action == "INSERT":
        ch = data
        ops.append(f"INSERT {cur_pos} {ch}")
        i, j = ni, nj
        cur_pos += 1  # inserted char shifts future positions

print("\n".join(ops))
