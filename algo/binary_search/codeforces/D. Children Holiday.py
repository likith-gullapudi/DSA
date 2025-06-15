m,n=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split()])
l,r=0,max([i[0]+i[2] for i in arr])*n
def check(mid):
    infloated = 0
    zz = []
    for t, z, y in arr:
        temp = (t * z + y)
        var = (mid // temp) * z
        rem= (mid % temp) // t
        if rem>=t*z:
            var+=z
        else:
            var+=rem//t
        infloated += var
        zz.append(var)
    if infloated >= m:
        return zz
    return []
ans=-1
while l<=r:
    mid=(l+r)//2
    #print(l, mid, r)
    temp=check(mid)

    if temp:
        ans=[mid,temp[:]]
        r=mid-1
    else:
        l=mid+1
print(ans[0])
for i in ans[1]:
    print(i,end=" ")
#print(check(1))
