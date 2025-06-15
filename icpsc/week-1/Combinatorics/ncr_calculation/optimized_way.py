n,r=[int(x) for x in input().split()]
ans=1
for i in range(r):
    ans=(ans*(n-r+i+1))/(i+1)
print(ans)