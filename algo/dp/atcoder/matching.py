def popcount(x):
    return bin(x).count('1')
MOD=10**9+7
n=int(input())
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split()])
MM=2**n
# dp=[[0 for i in range(MM)]for j in range(n+1)]
# for index in range(n,-1,-1):
#     for biset in range(MM-1,-1,-1):
#
#         if index!=n-popcount(biset):
#             continue
#         if index==n:
#             dp[n][biset]=int(biset==0)
#             continue
#         else:
#             j = 0
#             while (1 << j) <= biset:
#                 if biset & (1 << j) and arr[index][j]:
#                     dp[index][biset] += dp[index + 1][biset ^ (1 << j)]
#                 j += 1
#         dp[index][biset]%=MOD
dp=[0 for i in range(MM)]
for biset in range(MM):
    index=n-popcount(biset)
    if index==n:
        dp[biset]=int(biset==0)
        continue
    else:
        j = 0
        while (1 << j) <= biset:
            if biset & (1 << j) and arr[index][j]:

                dp[biset] += dp[biset ^ (1 << j)]
                dp[biset] %= MOD
            j += 1
print(dp[MM-1])
