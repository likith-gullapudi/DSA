MOD=10**9+7
n,q=[int(x) for x in input().split()]
arr=[int(x)%MOD for x in input().split()]
a=[0 for i in range(n+1)]
b=[0 for i in range(n+1)]
for i in range(1,n+1):
    a[i]=a[i-1]+arr[i-1]
    b[i]=b[i-1]+arr[i-1]*i
    a[i]%=MOD
    b[i]%=MOD
for _ in range(q):
    l,r=[int(x) for x in input().split()]
    x=b[r]-b[l-1]
    y=(1-l)*(a[r]-a[l-1])
    x%=MOD
    y%=MOD
    print((x+y)%MOD)

