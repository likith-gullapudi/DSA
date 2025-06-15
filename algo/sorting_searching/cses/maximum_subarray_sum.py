n=int(input())
arr=[int(x) for x in input().split()]
s=ans=arr[0]
s=max(s,0)
for j in range(1,len(arr)):
    i=arr[j]
    s+=i
    #print(j,s)
    ans=max(ans,s)
    s=max(s,0)
print(ans)