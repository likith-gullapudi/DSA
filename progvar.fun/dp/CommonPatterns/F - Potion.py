from functools import lru_cache

n,x=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
#dp[i][took]-->means we are on index i,took t already and toit return from i t0 n-1 how much time it will take
#base case dp[n][took]=x
#total=sum+k*t
#total-sum should be divisible by t
#so total%k=sum%k

#dp[i][took] we are on inde
#can i think like max sum you can get from all poritions by selecting k portions such that sum is in form of
#(total-x*k)%k that is max sum should be like total%k(since k<=100 it will be ok)
#so basically for every possible k we have to find max sum using k takes and total%k=0

d={}
def fun(i,k,m):
    if (i,k,m) in d:
        return d[(i,k,m)]
    if k==0:
        # print(i,K,m,x%K)
        return 0 if m == x%K else -float('inf')
    if i==n:
        return -float("inf")

    a=arr[i]+fun(i+1,k-1,(m+arr[i])%K)
    b=fun(i+1,k,m)
    d[(i,k,m)]=max(a,b)
    return d[(i,k,m)]
ans=float('inf')
for K in range(1,n+1):
    d={}
    temp=fun(0,K,0)
    # print(K,temp,x-temp)
    if temp!=-float("inf"):
        ans=min(ans, (x-temp)//K)
print(ans)
