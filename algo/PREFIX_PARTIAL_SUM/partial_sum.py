#lets use 1 based indexing
n,k,q=[int(x) for x in input().split()]
arr=[0 for i in range(100005)]
for _ in range(q):
    l,r=[int(x) for x in input().split()]
    arr[l]+=1
    arr[r+1]-=1
helper=0
pre=[0 for i in range(n+1)]
for i in range(1,n+1):
    arr[i]+=arr[i-1]
    pre[i]=pre[i-1]+int(arr[i]>=k)
for _ in range(q):
    l,r=[int(x) for x in input().split()]
    print(pre[r]-pre[l-1])

