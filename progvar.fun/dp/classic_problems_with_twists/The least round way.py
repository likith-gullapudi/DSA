n=int(input())
arr=[]
m=-1
for _ in range(n):
    arr.append([int(x) for x in input().split()])
    m=max(m,max(arr))
#dp[i][j]-min number of two factors from (i,j) to (n-1,n-1)
#base case dp[n-1][n-1]=find how many  2's in this number
#dp[i][j]=fun(num)+min(dp[i+1,j],dp[i,j+1])
def fun(i,j,div):
    ans=0
    while arr[i][j] and arr[i][j]%div==0:
        ans+=1
        arr[i][j]//=div
    return ans
# Initialize DP and path tables
# dp = [[[[float('inf'), ''], [float('inf'), '']] for _ in range(n + 1)] for _ in range(n + 1)]
# path = [[['', ''] for _ in range(n + 1)] for _ in range(n + 1)]
present=[[[float('inf'), ''], [float('inf'), '']] for _ in range(n + 1)]
next=[[[float('inf'), ''], [float('inf'), '']] for _ in range(n + 1)]
# Function to reconstruct path from stored directions
# two_powers=[]
# five_powers=[]
# temp=1
# while temp<m:



# Start filling dp from bottom-right to top-left
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if i == n - 1 and j == n - 1:
            # Base case: bottom-right cell
            present[j][0] = [fun(i, j, 2), '']  # Store both value and empty path
            present[j][1] = [fun(i, j, 5), '']
            continue

        # DP for power of 2 (index 0)
        if i + 1 < n and j < n and next[j][0][0] < present[j + 1][0][0]:
            # Down is better
            present[j][0][0] = fun(i, j, 2) + next[j][0][0]
            present[j][0][1] = 'D' + next[j][0][1]
            # path[i][j][0] = 'D'
        else:
            # Right is better or only option
            present[j][0][0] = fun(i, j, 2) + present[j + 1][0][0]
            present[j][0][1] = 'R' + present[j + 1][0][1]
            # path[i][j][0] = 'R'

        # DP for power of 5 (index 1)
        if i + 1 < n and j < n and next[j][1][0] < present[j + 1][1][0]:
            # Down is better
            present[j][1][0] = fun(i, j, 5) + next[j][1][0]
            present[j][1][1] = 'D' + next[j][1][1]
            # path[i][j][1] = 'D'
        else:
            # Right is better or only option
            present[j][1][0] = fun(i, j, 5) + present[j + 1][1][0]
            present[j][1][1] = 'R' + present[j + 1][1][1]
            # path[i][j][1] = 'R'
    next=present[:]
# print(present[0])
if present[0][0][0]<=present[0][1][0]:
    print(present[0][0][0])
    print(present[0][0][1])
else:
    print(present[0][1][0])
    print(present[0][1][1])


