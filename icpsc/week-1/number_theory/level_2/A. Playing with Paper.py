a,b=[int(x) for x in input().split()]
a,b=max(a,b),min(a,b)
ans=0
while a!=0 and b!=0 and a!=b:
    ans+=a//b
    a,b=b,a%b
    #print(a,b)
print(ans)