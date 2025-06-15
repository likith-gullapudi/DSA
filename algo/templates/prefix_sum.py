MOD=10**9+7

n,q=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
pre=[0 for i in range(n+1)]
for i in range(1,n+1):
    pre[i]=arr[i-1]+pre[i-1]#arr[i-1] present element(pre moved one step forward) pre[i-1]prefix sum for beloe element
    pre[i]%=MOD
for _ in range(q):
    l,r=[int(x) for x in input().split()]
    print((pre[r]-pre[l-1])%MOD)