import bisect
print(bisect.bisect_left([1],2))
n=int(input())
arr=[int(x) for x in input().split()]
towers=[]
print(bisect.bisect_left([1],1))
for i in arr:
    if towers==[]:
        towers.append(i)
        continue
    x=bisect.bisect_left(towers,i)
    print(x,towers)

    if x==-1:
        towers.insert(0,i)
    else:
        towers[x]=i

print(len(towers))
