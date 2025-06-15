n=int(input())
arr=[]
for _ in range(n):
    arr.append([int(x) for x in input().split()])
arr.sort(key=lambda x:x[1])
prev=-1
ans=0
for st,end in arr:
    if st>=prev:
        prev=end
        ans+=1
print(ans)
