import sys

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    head=-1
    tail=ans=0
    d={}
    distinct=0
    while tail<n:
        while head+1<n and (distinct<k or arr[head+1] in d):
            head += 1
            if arr[head] in d:
                d[arr[head]]+=1
            else:
                d[arr[head]]=1
                distinct+=1
        ans+=head-tail+1
        #print(tail, head, arr[tail:head + 1],ans)
        if head<tail:
            tail+=1
            head=tail-1
        else:
            d[arr[tail]]-=1
            if d[arr[tail]]==0:
                distinct-=1
                del d[arr[tail]]
            tail+=1
    print(ans)




