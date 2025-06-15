s=input()
t=input()
n,m=len(s),len(t)

present=[0 for i in range(m+1)]
next=[0 for i in range(m+1)]

for i in range(n,-1,-1):
    for j in range(m,-1,-1):
        if i==n:
            present[j]=m-j
            continue
        if j==m:
            present[j]=n-i
            continue
        ans=float('inf')
        if s[i]==t[j]:
            ans=min(ans,next[j+1] )
        ans=min(ans,1+next[j],1+next[j+1],1+present[j+1])
        present[j]=ans
    next=present[:]
print(present[0])

