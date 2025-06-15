n=int(input())
r=12
ans=1
for i in range(r-1):
    ans=(ans*(n-r+i+1))//(i+1)
print(ans)