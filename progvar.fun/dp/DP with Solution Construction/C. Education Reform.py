
n,m,k=[int(x) for x in input().split()]
arr=[]
for _ in range(m):
    arr.append([int(x) for x in input().split()]+[_])
# print(arr)
arr.sort(key=lambda x:x[2])
print(arr)
d={}
def fun(index,prev_tasks,taken):
    if (index,prev_tasks,taken) in d:
        return d[(index,prev_tasks,taken)]
    if taken==n:
        return 0
    if index==m:
        return -float('inf')
    ans=-float('inf')
    temp=[]
    if taken!=0:
        temp=[prev_tasks+k,prev_tasks*k]
    else:
        temp=[i for i in range(arr[index][0],arr[index][1]+1)]
    for new_tasks in temp:
        if arr[index][0]<=new_tasks<=arr[index][1]:
            ans=max(ans,fun(index+1,new_tasks,taken+1)+new_tasks)
    ans=max(ans,fun(index+1,prev_tasks,taken))
    # print("here",index,prev_tasks,ans)
    d[(index, prev_tasks, taken)]=ans
    return ans
ans=fun(0,0,0)

print(fun(0,0,0))





