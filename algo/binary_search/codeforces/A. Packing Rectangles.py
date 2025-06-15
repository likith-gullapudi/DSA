he,w,n=[int(x) for x in input().split()]
l,h=1,max(he,w)*n+10
def check(x):
    #print(x,(x//he),(x//w),n)
    return (x//he)*(x//w)>=n
ans=-1
while l<=h:
    mid=(l+h)//2
    if check(mid):
        ans=mid
        h=mid-1
    else:
        l=mid+1
print(ans)