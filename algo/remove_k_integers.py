import sys

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    lo,hi=1,arr[-1]-arr[0]
    while lo<=hi:
        mid=(lo+hi)//2
        if (mid):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    print(ans)
