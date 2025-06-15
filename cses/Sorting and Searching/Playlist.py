n=int(input())
arr=[int(x) for x in input().split()]
d={}
l,r=0,-1
ans=0
while l<n:
    while r+1<n and d.get(arr[r+1],0)==0:
        d[arr[r+1]]=1
        r+=1
        ans=max(ans,r-l+1)
    d[arr[l]]-=1
    l+=1
print(ans)


