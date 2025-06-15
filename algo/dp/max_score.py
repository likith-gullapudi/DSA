def fun(index,col,s):
    if not 0<=col<m:
        return -float('inf')

    if index==-1:
        if s==0:
            return 0
        return -float('inf')
    ans=max(fun(index-1,col-1,(s+arr[index][col])%k),fun(index-1,col+1,(s+arr[index][col])%k))+arr[index][col]
    return ans
for _ in range(int(input())):
    n,m,k=[int(x) for x in input().split()]
    arr=[]
    for _ in range(n):
        arr.append([int(x) for x in input()])

    ans=max(fun(n-1,col,arr[0][col]%k) for col in range(m))
    print(ans)

