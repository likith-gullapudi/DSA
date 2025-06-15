n=int(input())
arr=[int(x) for x in input().split()]
count=[0,0,0,0]
for i in arr:
    count[i]+=1
dp=[[[-1 for i in range(n+1)] for j in range(n+1)] for z in range(n+1)]
for threes in range(n+1):
    for twos in range(n+1):
        for ones in range(n+1):
            if threes==0 and ones==0 and twos==0:
                dp[ones][twos][threes]=0
                continue
            else:

                dp[ones][twos][threes]=n+(ones/n*dp[ones-1][twos][threes] if ones>0  else 0)\
                                       +(twos/n*dp[ones+1][twos-1][threes] if twos>0 and ones+1<n else 0)\
                                       +(threes/n*dp[ones][twos+1][threes-1] if threes>0 and twos+1<n else 0)
for i in dp:
    print(i)
print(dp[count[1]])
print(dp[count[1]][count[2]][count[3]])