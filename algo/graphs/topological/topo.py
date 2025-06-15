import heapq

n,m=[int(x) for x in input().split()]
arr=[[] for i in range(n)]
indegree=[0 for i in range(n)]
ans=[]
for _ in range(m):
    x,y=[int(x)-1 for x in input().split()]
    arr[x].append(y)
    indegree[y]+=1
q=[]
for i in range(n):
    if indegree[i]==0:
        heapq.heappush(q,i)
while q:
    temp=heapq.heappop(q)
    ans.append(str(temp+1))
    for nei in arr[temp]:
        indegree[nei]-=1
        if indegree[nei]==0:
            heapq.heappush(q,nei)
if len(ans)==n:
    print(" ".join(ans))
else:
    print(-1)



