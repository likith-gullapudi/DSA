from collections import Counter

n=int(input())
arr=[int(x) for x in input().split()]
d={}
for i in range(len(arr)):
    d[arr[i]]=i
ans=0
prev=-1
for i in range(1,n+1):
    if d[i]<=prev:
        ans+=1
    prev=d[i]
print(ans+1)