from sortedcontainers import SortedList
n,k=[int(x) for x in input().split()]

watchers=SortedList([0] * k)
movies=[]
ans=0
for _ in range(n):
    movies.append([int(x) for x in input().split()])
movies.sort(key=lambda x:x[1])
for st,en in movies:
    #find some watcher recentlu ended
    idx = watchers.bisect_right(st)
    if idx == 0:
        continue  # No watcher is free before movie starts
    watchers.pop(idx - 1)  # Assign movie to the watcher who becomes free just before start
    watchers.add(en)  # Update that watcher’s next free time
    ans+=1
print(ans)


