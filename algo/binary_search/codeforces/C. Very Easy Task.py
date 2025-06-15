n,x,y=[int(x) for x in input().split()]
time=min(x,y)
n-=1
l,h=0,max(x,y)*n
def check(mid):
    temp=mid//x+mid//y
    return temp>=n
ans=-1
while l<=h:
    mid=(l+h)//2
    if check(mid):
        ans=mid
        h=mid-1
    else:
        l=mid+1
#print(check(1))
print(ans+min(x,y))