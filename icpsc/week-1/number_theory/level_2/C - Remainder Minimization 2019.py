import heapq

l,r=[int(x) for x in input().split()]

if r-l>=2019:
    print(0)
else:
    ans=float('inf')
    for i in range(l,r+1):
        for j in range(l+1,r+1):
            ans=min(ans,(i*j)%2019)
    print(ans)

