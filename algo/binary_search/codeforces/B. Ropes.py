#B. Ropes
n,k=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append(int(input()))
l,r=1,max(arr)
ans=1
def check(mid):
    #print(mid)
    temp=0
    for i in arr:
        temp+=i//mid
    return temp>=k
while r-l>=10**-10:

    mid=(l+r)/2
    #print(l,r,mid,check(mid))
    if check(mid):
        ans=mid
        l=mid
    else:
        r=mid
print(ans)



