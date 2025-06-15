# n=int(input())
# arr=[]
# for _ in range(n):
#     arr.append([int(x) for x in input().split()])
# dp=[[-1 for i in range(3)] for j in range(n+1)]
# for index in range(n,-1,-1):
#     for prev in range(3):
#         if index==n:
#             dp[index][prev]=0
#             continue
#         dp[index][prev]=-float('inf')
#         for present in range(3):
#             if present!=prev:
#                 dp[index][prev]=max(dp[index][prev],dp[index+1][present]+arr[index][present])
# ans=max(  dp[1][0]+arr[0][0],dp[1][1]+arr[0][1],dp[1][2]+arr[0][2]  )
# print(ans)
n=int(input())
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split()])
dp=[[-1 for i in range(3)] for j in range(n+1)]
for index in range(n):
    for present in range(3):
        if index==0:
            dp[index][present]=arr[0][present]
            continue
        else:
            dp[index][present]=-float('inf')
            for prev in range(3):
                if prev!=present:
                    dp[index][present]=max( dp[index][present],dp[index-1][prev]+arr[index][present])
print(max(dp[n-1]))