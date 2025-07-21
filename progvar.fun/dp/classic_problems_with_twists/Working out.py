n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Initialize 4 DP tables
dp1 = [[0]*m for _ in range(n)]  # From (0,0) to (i,j)
dp2 = [[0]*m for _ in range(n)]  # From (n-1,0) to (i,j)
dp3 = [[0]*m for _ in range(n)]  # From (n-1,m-1) to (i,j)
dp4 = [[0]*m for _ in range(n)]  # From (0,m-1) to (i,j)

# Fill dp1: top-left to bottom-right
for i in range(n):
    for j in range(m):
        if i > 0:
            dp1[i][j] = max(dp1[i][j], dp1[i-1][j])
        if j > 0:
            dp1[i][j] = max(dp1[i][j], dp1[i][j-1])
        dp1[i][j] += a[i][j]

# Fill dp2: bottom-left to top-right
for i in reversed(range(n)):
    for j in range(m):
        if i < n-1:
            dp2[i][j] = max(dp2[i][j], dp2[i+1][j])
        if j > 0:
            dp2[i][j] = max(dp2[i][j], dp2[i][j-1])
        dp2[i][j] += a[i][j]

# Fill dp3: bottom-right to top-left
for i in reversed(range(n)):
    for j in reversed(range(m)):
        if i < n-1:
            dp3[i][j] = max(dp3[i][j], dp3[i+1][j])
        if j < m-1:
            dp3[i][j] = max(dp3[i][j], dp3[i][j+1])
        dp3[i][j] += a[i][j]

# Fill dp4: top-right to bottom-left
for i in range(n):
    for j in reversed(range(m)):
        if i > 0:
            dp4[i][j] = max(dp4[i][j], dp4[i-1][j])
        if j < m-1:
            dp4[i][j] = max(dp4[i][j], dp4[i][j+1])
        dp4[i][j] += a[i][j]

# Try all possible meeting points
ans = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        # Two valid path combinations around the meeting point (i,j)
        option1 = dp1[i][j-1] + dp3[i][j+1] + dp2[i+1][j] + dp4[i-1][j]
        option2 = dp1[i-1][j] + dp3[i+1][j] + dp2[i][j-1] + dp4[i][j+1]
        ans = max(ans, option1, option2)

print(ans)
