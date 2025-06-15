MOD=10**9+7
n,q=[int(x) for x in input().split()]

x=[0 for i in range(n+2)]
y=[0 for i in range(n+2)]
for _ in range(q):
    a, d, l, r = [int(x) for x in input().split()]
    x[l]+=a-l*d
    x[r+1]-=(a-l*d)
    y[l]+=d
    y[r+1]-=d
for i in range(1,n+1):
    x[i]+=x[i-1]
    y[i]+=y[i-1]
for i in range(1,n+1):
    y[i]*=i
for i in range(1,n+1):
    print((x[i]+y[i])%MOD,end=" ")

