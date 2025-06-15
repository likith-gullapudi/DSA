import math

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
factors=0
for i in range(1,n+1):
    #find prime factors
    while i>=1:
        d[spf[i]]=d.get(spf[i],0)+1
        if i==1:
            break
        i//=spf[i]

print(d,len(d))
