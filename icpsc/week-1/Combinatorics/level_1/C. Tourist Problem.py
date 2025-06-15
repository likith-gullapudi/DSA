import math

n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
ans=0
prefix_sum=[i for i in arr]
for i in range(1,n):
    prefix_sum[i]+=prefix_sum[i-1]
for i in range(n-1,0,-1):
    ans+=(i*arr[i])-prefix_sum[i-1]
    # print(i,ans)
    #
    # for j in range(i+1,n):
    #     ans+=abs(arr[i]-arr[j])
# print(ans)
ans*=2*(n-1)
for i in range(n):
    ans+=(n-1)*arr[i]
num,den=ans,n*(n-1)
# print(num,den)
g=math.gcd(num,den)
print(num//g,den//g)