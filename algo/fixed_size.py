import sys
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    d={}
    for i in arr[:k]:
        d[i]=d.get(i,0)+1
    ans=len(d)
    for i in range(k,len(arr)):

        d[arr[i]]=d.get(arr[i],0)+1
        d[arr[i-k]]-=1
        if d[arr[i-k]]==0:
            del d[arr[i-k]]
        ans=min(ans,len(d))
    print(ans)

