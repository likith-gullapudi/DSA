#https://atcoder.jp/contests/abc079/tasks/abc079_b
from functools import cache
n=int(input())
dp=[-1 for i in range(n+1)]
dp[0],dp[1]=2,1
@cache
def fun(index):
    if dp[index]!=-1:
        return dp[index]
    dp[index]=fun(index-1)+fun(index-2)
    return dp[index]
print(fun(n))
