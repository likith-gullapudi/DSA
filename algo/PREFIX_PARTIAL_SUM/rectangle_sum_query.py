MOD=10**9+7
n,m,q=[int(x) for x in input().split()]
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split()])
pre=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        pre[i][j]=pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+arr[i-1][j-1]
        pre[i][j]%=MOD


for _ in range(q):
    x1,y1,x2,y2=[int(x) for x in input().split()]
    print((pre[x2][y2]-pre[x1-1][y2]-pre[x2][y1-1]+pre[x1-1][y1-1])%MOD)

