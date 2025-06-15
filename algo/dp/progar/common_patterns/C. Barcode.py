n,m,x,y=[int(x) for x in input().split()]
mat=[]
for _ in range(n):
    mat.append([x for x in input()])
#cost[i] means chaing all mat[i] to #
cost=[0 for i in range(m)]
for j in range(m):
    temp=0
    for i in range(n):
        temp+=1 if mat[i][j]=='.' else 0
    cost[j]=temp
prefix_cost=[0 for i in range(m)]
prefix_cost[0]=cost[0]
for i in range(1,m):
    prefix_cost[i]=prefix_cost[i-1]+cost[i]
prefix_cost.append(prefix_cost[-1])
#dp[i][0/1] means cost from Ith column starting with 0/1
dp=[[float('inf') for i in range(2)] for j in range(m+1)]
#print(prefix_cost)
for i in range(m,-1,-1):
    for j in range(2):
        if i==m:
            dp[i][j]=0
            continue
        if i+x-1>=m:
            dp[i][j]=float('inf')
            continue

        for k in range(i+x-1,min(m,i+y)):
            cost_to_change=prefix_cost[k]-(prefix_cost[i-1] if i-1>=0 else 0)
            if j==1:
                cost_to_change=n*(k-i+1)-cost_to_change
            #print(k)
            dp[i][j]=min(dp[i][j],dp[k+1][j^1]+cost_to_change)
        #print(j, i,dp[i][j])
#print(dp)
print(min(dp[0]))

