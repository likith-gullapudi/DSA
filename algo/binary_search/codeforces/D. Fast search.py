#D. Fast search
n=int(input())
arr=[int(x) for x in input().split()]
k=int(input())
arr.sort()
def fun(target):
    ans=-1
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<target:
            ans=mid
            l=mid+1
        else:
            r=mid-1
    #print(arr,target,ans)
    return ans
for _ in range(k):
    l,r=[int(x) for x in input().split()]
    print(fun(r+1)-fun(l))
