t=int(input())
arr=[]
n=-float('inf')
m=10**9
for _ in range(t):
    arr.append(int(input()))
    n=max(n,arr[-1])



table=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(i+1):
        if i==0 or j==0:
            table[i][j]=1
            continue
        table[i][j]=(table[i-1][j-1]+table[i-1][j])%m
for n in arr:
    for j in range(n+1):
        print(table[n][j],end=" ")
    print()
