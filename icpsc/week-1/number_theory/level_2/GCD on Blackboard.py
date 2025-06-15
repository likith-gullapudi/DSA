import math

n=int(input())
arr=[int(x) for x in input().split()]
prefix_gcd=[int(x) for x in arr]
for i in range(1,n):
    prefix_gcd[i]=math.gcd(prefix_gcd[i-1],arr[i])
suffix_gcd=[int(x) for x in arr]
for i in range(n-2,-1,-1):
    suffix_gcd[i]=math.gcd(suffix_gcd[i+1],arr[i])

ans=suffix_gcd[1]
for i in range(1,n-1):
    ans=max(ans,math.gcd(prefix_gcd[i-1],suffix_gcd[i+1]))
ans=max(ans,math.gcd(prefix_gcd[n-2]))
print(ans)



