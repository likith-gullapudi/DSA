n=int(input())
arr=[int(x) for x in input().split()]
towers=[]
def fun(towers,i):
    #just greater than i
    #print(towers)
    lo,hi=0,len(towers)-1
    ans=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if towers[mid]>i:
            hi=mid-1
            ans=mid
        else:
            lo=mid+1
    return ans


for i in arr:
    index=fun(towers,i)
    #print(index)
    if index==-1:
        towers.append(i)
    else:
        towers[index]=i
print(len(towers))