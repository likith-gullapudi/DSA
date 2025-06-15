n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
left,right=0,-1
d={}
ans=0
left,right=0,0
while right<n:
    d[arr[right]] = d.get(arr[right], 0) + 1
    while left<=right and len(d)>k:
        d[arr[left]]-=1
        if d[arr[left]]==0:
            del d[arr[left]]
        left+=1
    ans+=right-left+1

    right+=1


print(ans)