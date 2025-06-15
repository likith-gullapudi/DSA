import math
import sys
sys.setrecursionlimit(10**5)
N,M,K=[int(x) for x in input().split()]
mod = 998244353
res = 0
for k in range(0, K + 1):
    ways = math.comb(N - 1, k) % mod
    ways = (ways * M) % mod
    ways = (ways * pow(M - 1, N - 1 - k, mod)) % mod
    res = (res + ways) % mod
print(res)



# def fun(n,k,first):
#     if k<0:
#         return 0
#     if n==0:
#         return 1
#     if (n,k,first) in d:
#         return d[(n,k,first)]
#     if first:
#         ans=m*fun(n-1,k,False)
#     else:
#         ans=(m-1)*fun(n-1,k,False)
#         ans+=fun(n-1,k-1,False)
#     ans%=mod
#     d[(n, k, first)]=ans
#     # print(n,k,ans)
#     return ans
