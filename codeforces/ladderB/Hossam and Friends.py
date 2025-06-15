for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    d={}
    for _ in range(m):
        a,b=[int(x)-1 for x in input().split()]
        a,b=min(a,b),max(a,b)
        d[a]=min(d.get(a,float("inf")),b)
        # d[b]=min(d.get(b,float("inf")),a)
    l,r=0,-1
    ans=0
    temp={}
    s=set()
    while l<n:
        while r+1<n:
            if r+1 in s:
                break
            else:
                if r+1 in d:
                    temp[d[r+1]]=temp.get(d[r+1],0)+1
                    if temp[d[r+1]]==1:
                        s.add(d[r+1])
                r+=1
        if l>r:
            l+=1
            r=l-1
            continue
        ans+=r-l+1
        # print(l, r, ans,temp,s,d)
        if l in d:
            temp[d[l]]-=1
            if temp[d[l]]==0:
                s.remove(d[l])
        l+=1


    print(ans)

