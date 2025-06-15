import sys
import bisect
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * n
    prefix[0] = int(arr[0] == 0)
    ans = 1

    for i in range(1, len(arr)):
        prefix[i] += int(arr[i] == 0) + prefix[i - 1]

    for i in range(len(arr)):
        temp = bisect.bisect_right(prefix,k+prefix[i-1] if i-1>=0 else k)
        ans = max(ans, temp - i)

    print(ans)
'''
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    ans=0
    head,tail=-1,0
    temp=0
    while tail<n:
        while head+1<n and temp+int(arr[head+1]==0)<=k:
            temp+=int(arr[head+1]==0)
            head+=1
        ans=max(ans,head-tail+1)
        if head>=tail:
            if arr[tail]==0:
                temp-=1
            tail+=1
        else:
            tail+=1
            head=tail-1
    print(ans)
'''