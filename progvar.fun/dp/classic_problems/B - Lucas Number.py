#https://atcoder.jp/contests/abc079/tasks/abc079_b

#memo
n=int(input())
dp=[-1 for i in range(n+1)]
# def fun(n):
#     if dp[n]!=-1:
#         return dp[n]
#     if n==0:
#         return 2
#     if n==1:
#         return 1
#     dp[n]=fun(n-1)+fun(n-2)
#     return dp[n]
# print(fun(n))

#tabulation
dp[0]=2
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])