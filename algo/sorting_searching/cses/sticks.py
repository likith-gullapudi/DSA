n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
mid=arr[n//2]

ans=0
for i in arr:
    ans+=abs(i-mid)
print(ans)