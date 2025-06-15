def fun(l):
    return l[0]*l[1]
for _ in range(int(input())):
    n,m=[int(x) for x  in input().split()]
    ans=0
    d={}
    for _ in range(n):
        temp=fun([int(a) for a in input().split()])
        d[temp]=d.get(temp,0)+1

    for _ in range(m):
        temp=fun([int(a) for a in input().split()])
        if d.get(temp,0)>=1:
            ans+=1
            d[temp]-=1
    print(ans)

