import math
import sys
def check(arr,n,k,ind):
    tail,head=0,-1
    s=ans=0
    while tail<n:
        while head+1<n and s+arr[head+1]<=k:
            head+=1
            s+=arr[head]
        ans+=head-tail+1
        if tail>head:
            tail+=1
            head=tail-1
        else:
            s-=arr[tail]
            tail+=1

    return ans>=ind


for _ in range(int(sys.stdin.readline())):

    n=int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    temp=(n*(n+1))//2
    k=math.ceil(temp/2)
    print(k)
    lo=0
    hi=sum(arr)
    ans=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if check(arr,n,mid,k):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    print(ans)
