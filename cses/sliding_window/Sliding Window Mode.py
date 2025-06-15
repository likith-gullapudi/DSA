from sortedcontainers import SortedList
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
s=SortedList()
d={}
for i in range(k):
    if  d.get(arr[i],0)==0:
        d[arr[i]]=d.get(arr[i],0)+1
        s.add((d[arr[i]],-arr[i]))
    else:
        s.remove((d[arr[i]],-arr[i]))
        d[arr[i]]+=1
        s.add((d[arr[i]],-arr[i]))
print(-s[-1][1],end=" ")
for i in range(k,n):
    if  d.get(arr[i],0)==0:
        d[arr[i]]=d.get(arr[i],0)+1
        s.add((d[arr[i]],-arr[i]))
    else:
        s.remove((d[arr[i]],-arr[i]))
        d[arr[i]]+=1
        s.add((d[arr[i]],-arr[i]))
    #removing
    s.remove((d[arr[i-k]],-arr[i-k]))
    d[arr[i-k]]-=1
    if d[arr[i-k]]!=0:
        s.add((d[arr[i-k]],-arr[i-k]))
    print(-s[-1][1],end=" ")



