n,x=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
arr.sort()
i,j=0,len(arr)-1
ans=0
while i<j:
    if arr[j]+arr[i]<=x:
        i+=1
        j-=1
    else:
        j-=1
    ans+=1
if i==j:
    ans+=1
print(ans)