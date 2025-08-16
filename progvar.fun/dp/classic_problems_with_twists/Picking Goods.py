#dp[i][j][taken] we are on i th row and jth column and we took taken already in this row
#base case dp[r][c][t]=0 if t>=3 or (i,j) not in points else 1
#dp[i][j][taken]=dp[i+1][j][
R,C,K=[int(x) for x in input().split()]
d={}
points=set()
dp=[[[-float('inf') for i in range(4)]for j in range(C+2)] for j in range(R+2)]
for _ in range(K):
    x,y,v=[int(x) for x in input().split()]
    points.add((x,y))
    d[(x,y)]=v
# print(points,d)
for r in range(R,-1,-1):
    for c in range(C,-1,-1):
        for taken in range(3,-1,-1):
            if r==R and c==C:
                dp[r][c][taken]=0 if (taken>=3 or (r,c) not in points) else d[(r,c)]
                continue
            else:
                #take
                if taken<=2 and (r,c) in points:
                    dp[r][c][taken]=max(dp[r][c][taken],dp[r][c+1][taken+1]+d[(r,c)])
                    dp[r][c][taken]=max(dp[r][c][taken],dp[r+1][c][0]+d[(r,c)])
                #not_take
                dp[r][c][taken]=max(dp[r][c][taken],dp[r][c+1][taken])
                dp[r][c][taken]=max(dp[r][c][taken],dp[r+1][c][0])
        # print(dp[c])
print(dp[0][0][0])




