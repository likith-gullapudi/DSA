#B. The Meeting Place Cannot Be Changed
n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
l,h=0,10**10
def check(t):
    l,r=0,1<<30
    for x in range(n):
        l=max((a[x]-b[x]*t),l)
        r=min((a[x]+b[x]*t),r)
    return l<=r
ans=10**9
while h-l>=10**-9:

    mid=(h+l)/2
    if check(mid):
        ans=mid
        h=mid
    else:
        l=mid
print(ans)

