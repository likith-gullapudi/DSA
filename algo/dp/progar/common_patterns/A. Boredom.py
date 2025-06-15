from collections import Counter

n=int(input())
arr=[int(x) for x in input().split()]
d=Counter(arr)
d = dict(sorted(d.items()))
l=[(i,j) for i,j in d.items()]
dp=[[-1 for i in range(2)] for j in range(len(d)+1)]
#print(l)
for i in range(len(d),-1,-1):
    for j in range(2):
        if i==len(d):
            dp[i][j]=0
            continue
        dp[i][j]=dp[i+1][0]
        if j==0 or (i-1<0 or l[i-1][0]+1!=l[i][0]):
            #print(j,i-1>=0 , l[i-1][0]+1!=l[i][0])
            dp[i][j]=max(dp[i][j],dp[i+1][1]+l[i][0]*l[i][1] )
print(dp[0][0])


