n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
q=[int(x) for x in input().split()]
def fun(target):
    l,r=0,len(arr)-1
    ans=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>=target:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    #print(arr[ans],target)
    return arr[ans]==target
for i in q:
    print('YES' if fun(i) else 'NO')


