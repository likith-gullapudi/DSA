def check(mid):
    ans=0
    for i in arr:
        ans+=(mid//i)
    return ans>=t

n,t=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
lo,hi=min(arr),min(arr)*t
ans=hi
while lo<=hi:
    mid=(lo+hi)//2
    #print(lo,hi,mid,check(mid))
    if check(mid):
        ans=mid
        hi=mid-1
    else:
        lo=mid+1
print(ans)