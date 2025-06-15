n,r=[int(x) for x in input().split()]
table=[[0 for i in range(r+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(min(i,r)+1):
        if i==0 or j==0:
            table[i][j]=1
            continue
        table[i][j]=table[i-1][j-1]+table[i-1][j]
print(table)
print(table[n][r])