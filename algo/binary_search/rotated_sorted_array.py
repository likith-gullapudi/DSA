for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    if len(arr)==1 or  arr[-1]<arr[-2]:
        print(arr[-1])
    else:
        lo,hi=0,n-2
        ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if arr[mid]<arr[0]:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        print(ans)


