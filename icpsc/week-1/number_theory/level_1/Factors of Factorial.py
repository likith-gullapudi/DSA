n=int(input())
mod=10**9+7
spf=[i for i in range(n+1)]
for i in range(2,n+1):
    if spf[i]!=i:
        continue
    for j in range(i,n+1,i):
        if spf[j]==j:
            spf[j]=i
d={}
for i in range(2,n+1):
    #find prime factors
    while i>1:
        d[spf[i]]=d.get(spf[i],0)+1
        i//=spf[i]
ans=1
for val in d.values():
    ans*=(val+1)
    ans%=mod
#print(d)
print(ans)