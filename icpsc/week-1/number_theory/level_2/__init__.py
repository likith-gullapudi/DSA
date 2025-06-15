# for i in range(1,100):
#     print(i,(4*i+3)%7)
n=int(input())
arr=[int(x) for x in input().split()]
# arr.sort()
# x='unknown'
# equ=arr[-1]*x+arr[-1]-1
#to find x can we try every
ans=-1
for m in range(1,2*max(arr)):
    temp=0
    for j in arr:
        temp+=(m%j)
    ans=max(ans,temp)
print(ans)