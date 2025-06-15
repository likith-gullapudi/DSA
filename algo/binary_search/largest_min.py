def check(mid):
    sitted=1
    prev=0
    for i in range(1,n):
        if arr[i]-arr[prev]>=mid:
            sitted+=1
            prev=i
    return sitted>=k



for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    lo, hi = 1, arr[-1] + arr[0] + 1
    ans=-1
    arr.sort()
    while lo <= hi:
        mid = (lo + hi) // 2
        temp = check(mid)
        # print(lo,mid,hi,temp)
        if temp:
            ans = mid
            lo=mid+1
        else:
            hi=mid-1
    print(ans)
