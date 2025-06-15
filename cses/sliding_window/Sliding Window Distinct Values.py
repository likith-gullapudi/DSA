n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
d={}
count=0
for i in range(k):
    d[arr[i]]=d.get(arr[i],0)+1
    count+=1 if d[arr[i]]==1 else 0
print(count,end=" ")
for i in range(k,n):
    d[arr[i]] = d.get(arr[i], 0) + 1
    count += 1 if d[arr[i]] == 1 else 0
    d[arr[i-k]]-=1
    count-=1 if d[arr[i-k]]==0 else 0
    print(count,end=" ")