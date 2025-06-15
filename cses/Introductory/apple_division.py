n=int(input())
arr=[int(x) for x in input().split()]
ans=float('inf')
def fun(index,s):
    global ans
    if index==n:
        if abs(s)<ans:
            ans=abs(s)
        return
    fun(index+1,s+arr[index])
    fun(index+1,s-arr[index])
fun(0,0)
print(ans)