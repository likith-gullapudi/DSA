n=int(input())
# print((2**n)%(10**9+7))
lo,hi=0,500
while lo<=hi:
    mid=(lo+hi)//2
    if 2**mid>10**9+7:
        ans=mid
        hi=mid-1
    else:
        lo=mid+1
print(2**30,2**30-10**9+7)