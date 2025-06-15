import math



for _ in range(int(input())):
    def check(x):
        p = 0
        for i in range(1, len(arr)):
            p+=math.ceil((arr[i]-arr[i-1])/x)-1
        #print(x,p)
        return p <= k
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]

    lo, hi = 1, arr[-1] - arr[0] + 1
    for i in range(1,len(arr)):
        hi=max(hi,arr[i]-arr[i-1])+1

    ans=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if check(mid):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    print(ans)



