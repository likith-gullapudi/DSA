n,x=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
d={}
for i in arr:
    if x-i in d:
        print(i,x-i)
        break
    d[i]=1
else:
    print("IMPOSSIBLE")