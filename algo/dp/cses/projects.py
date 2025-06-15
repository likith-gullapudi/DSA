import bisect

n=int(input())
d={}
m=-float('inf')
arr=[]
for _ in range(n):
    start,end,worth=[int(x) for x in input().split()]
    arr.append([start,end,worth])
    if start in d:
        d[start].append([end,worth])
    else:
        d[start]=[[end,worth]]
    m=max(m,end)
arr.sort()
start_times = [task[0] for task in arr]

memo=[0 for i in range(n+1)]
#print(arr)
for i in range(n,-1,-1):
    if i==n:
        memo[i]=0
    else:
        #not take
        memo[i]=max(memo[i+1],memo[i])
        #take
        next_index = bisect.bisect_right(start_times, arr[i][1])
        #print(next_index)
        memo[i]=max(memo[i],arr[i][2]+memo[next_index])
print(memo[0])
'''
#print(d)
dp=[0 for i in range(m+2)]
#form 2
#dp[days] max amount i can get by last days

for days in range(m,-1,-1):

    dp[days]=0
    if days in d:
        #print(d.get(days))

        for end,profit in d.get(days):
            dp[days]=max(dp[days],dp[end+1]+profit)
    dp[days]=max(dp[days],dp[days+1])
print(dp[1])
'''
