# import sys
# sys.setrecursionlimit(7*10**3)
n,m=[int(x) for x in input().split()]
arr=[]
for i in range(n):
    arr.append(int( [x for x in input().split()][0]))
# print(arr)
#dp[i][s] cost of i to n we are on s specie
#base case dp[n][...]=0

dp=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n,-1,-1):
    for s in range(m,-1,-1):
        if i==n:
            dp[i][s]=0
            continue
        ans=float('inf')
        if arr[i] < s:
            ans = min(ans, 1 + dp[i+1][s])
        elif arr[i] == s:
            ans = min(ans, dp[i+1][s])
        elif arr[i] > s:
            ans = min(ans, dp[i+1][arr[i]], 1 + dp[i+1][s])
        dp[i][s]=ans
#     print(i,dp[i])
# print(dp[0])
print(min(dp[0]))
'''
3 [0, 0, 0]
2 [0, 0, 1]
1 [0, 0, 2]
0 [1, 1, 2]
[1, 1, 2]
1'''

# def fun(i, s):
#     if dp[i][s]!=-1:
#         return dp[i][s]
#     if i == n:
#         return 0
#     ans=float('inf')
#     if arr[i]<s:
#         ans=min(ans,1+fun(i+1,s))
#     elif arr[i]==s:
#         ans=min(ans,fun(i+1,s))
#     elif arr[i]>s:
#         ans=min(ans,fun(i+1,arr[i]),1+fun(i+1,s))
#     dp[i][s]=ans
#     return ans


