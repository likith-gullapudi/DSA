for _ in range(int(input())):

    n,m=[int(x) for x in input().split()]
    arr=[]
    for _ in range(n):
        arr.append([int(x) for x in input().split()])
    def fun(i,j,health):

        if i==0 and j==0:
            return [arr[i][j],arr[i][j]>health]
        ans=-float('inf')
        if i-1>=0:
            a,b=fun(i-1,j,health)
            if b:
                ans=max(ans,arr[i][j]+a)
        if j-1>=0:
            a,b=fun(i,j-1,health)
            if b:
                ans=max(ans,arr[i][j]+a)
        #print(i,j,ans,ans>health)
        return [ans,ans>health]

    #print(fun(n-1,m-1,-3))
    #exit()

    ans=-1
    l,r=1,n*m*1001

    while l<=r:
        mid=(l+r)//2
        #print(l, r, -mid,fun(n-1, m-1, -mid))
        _,check=fun(n-1,m-1,-mid)
        if check:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)

