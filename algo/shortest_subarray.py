import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    k=len(set(arr))
    d={}
    temp=0
    head,tail=-1,0
    ans=n
    while tail<n:
        while head+1<n and (temp<k):
            head+=1
            if arr[head] in d:
                d[arr[head]]+=1
            else:
                d[arr[head]] = 1
                temp+=1
        if temp==k:
            ans=min(ans,head-tail+1)
        if tail>head:
            tail+=1
            head=tail-1
        else:
            d[arr[tail]]-=1
            if d[arr[tail]]==0:
                temp-=1
                del d[arr[tail]]
            tail+=1
    print(ans)




