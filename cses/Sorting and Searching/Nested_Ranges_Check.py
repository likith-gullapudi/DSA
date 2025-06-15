from sortedcontainers import SortedList
n=int(input())
arr=[]
end=SortedList()
for _ in range(n):
    arr.append([int(x) for x in input().split()]+[_])
    end.add(arr[-1][1])
arr.sort(key=lambda x:x[0])
ans = [[0 for _ in range(n)] for _ in range(2)]
new_end=SortedList()
for st,en,index in arr:
    #do you find any ending point that is before this st end point
    end.remove(en)
    idx = end.bisect_right(en) - 1
    if idx >= 0:
        ans[0][index]=1
    idx = new_end.bisect_left(en)
    if idx < len(new_end):
        ans[1][index] = 1
    new_end.add(en)

for i in ans:
    for j in i:
        print(j,end=" ")
    print()

