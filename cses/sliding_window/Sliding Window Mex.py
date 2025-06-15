from sortedcontainers import SortedList
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
s=SortedList([i for i in range(n+10)])
d={}
for i in range(k):
    if d.get(arr[i],0)==0:
        s.remove(arr[i])
    d[arr[i]]=d.get(arr[i],0)+1
print(s[0],end=" ")
for i in range(k,n):
    if d.get(arr[i],0)==0:
        s.remove(arr[i])
    d[arr[i]]=d.get(arr[i],0)+1
    d[arr[i-k]]-=1
    if d[arr[i-k]]==0:
        s.add(arr[i-k])
    print(s[0],end=" ")

