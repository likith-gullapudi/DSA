import heapq


def fun(a):
    return (a*(a-1))//2
for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    ans=fun(n)
    heap=[]

    for i,j in d.items():
        if j>1:
            ans -= fun(j)
            heapq.heappush(heap,-j)
    
    while k>0 and heap:
        fre=-heapq.heappop(heap)
        fre-=1
        if fre>1:
            heapq.heappush(heap,-fre)
        ans+=fre
        k-=1
    print(ans)






