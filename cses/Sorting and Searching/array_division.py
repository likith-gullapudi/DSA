n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
lo,hi=max(arr),sum(arr)

def check(mid):
    s=0
    breaked=0
    for num in arr:
        if s+num>mid:
            s=0
            breaked+=1
            if breaked==k:
                return False
        s+=num

    # print(breaked)
    return breaked<k
# print(check(7))
ans=sum(arr)
while lo<=hi:
    mid=(lo+hi)//2
    if check(mid):
        ans=mid
        hi=mid-1
    else:
        lo=mid+1
print(ans)