import sys

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    head=-1
    tail=ans=0
    sum=0
    while tail<n:
        while head+1<n and sum+arr[head+1]<=k:
            head += 1
            sum+=arr[head]
        ans+=head-tail+1

        if head<tail:
            tail+=1
            head=tail-1
        else:
            sum-=arr[tail]
            tail+=1
    print(ans)




