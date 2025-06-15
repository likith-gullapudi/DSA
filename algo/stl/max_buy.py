# import bisect
#
# n,q=[int(x) for x in input().split()]
# arr=[int(x) for x in input().split()]
# arr.sort()
# for i in range(1,len(arr)):
#     arr[i]+=arr[i-1]
# for _ in range(q):
#     x=int(input())
#     idx=bisect.bisect_right(arr,x)
#     #print(idx,len(arr))
#     if idx==len(arr):
#         print(idx)
#     elif arr[idx]==x:
#         print(idx+1)
#     else:
#         print(idx)
import bisect

n,q=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
arr.sort()
que=[]
for i in range(1,len(arr)):
    arr[i]+=arr[i-1]
for i in range(q):
    que.append([i,int(input())])
que.sort(key=lambda x:x[1])
temp=0
j=0
ans=[-1 for i in range(q)]

for index,val in que:
    while j<len(arr) and arr[j]<=val:

        j+=1
    ans[index]=j

for i in ans:
    print(i)
