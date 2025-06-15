class object:
    def __init__(self):
        self.t=0
        self.d=0
        self.p=0
        self.index=0
    def input_taking(self,arr,index):
        self.t=arr[0]
        self.d = arr[1]
        self.p = arr[2]
        self.index=index

n=int(input())
arr=[object() for i in range(n)]
s=0
for i in range(n):
    inp=[int(x) for x in input().split()]
    arr[i].t =inp[0]
    arr[i].d =inp[1]
    arr[i].p =inp[2]
    arr[i].index=i
    s+=arr[i].t

arr.sort(key=lambda x:x.d)
dp=[[-1 for i in range(s+1)] for j in range(n)]
path=[[-1 for i in range(s+1)] for j in range(n)]
def fun(index,time):
    if index==n:
        return 0
    if dp[index][time]!=-1:
        return dp[index][time]
    take=not_take=-float('inf')
    #take
    if time+arr[index].t<arr[index].d:
        take=fun(index+1,time+arr[index].t) +arr[index].p
    #not take
    not_take=fun(index+1,time)
    dp[index][time]=max(take,not_take)
    path[index][time]=0 if take>=not_take else 1
    return max(take,not_take)
ans=[]
def printsol(index,time,count):
    if index==n:
        print(count)
        return

    fun(index,time)
    if path[index][time]==0:

        printsol(index+1,time+arr[index].t,count+1)
        ans.append(arr[index].index+1)
    else:
        printsol(index+1,time,count)

print(fun(0,0))
printsol(0,0,0)
print(" ".join([str(k) for k in ans[::-1]]))



