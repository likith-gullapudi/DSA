n=int(input())
arr=[0 for i in range(n)]
for _ in range(n-1):
    x,y=[int(x)-1 for x in input().split() ]
    arr[x]+=1
    arr[y]+=1
print(max(arr)+1)
