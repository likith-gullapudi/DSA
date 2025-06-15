def fun(s):
    if s<0:
        return 0
    if s==0:
        return 1 
    ans=0
    for i in range(1,7):
        ans+=fun(s-i)
    return ans
n=int(input())
print(fun(n))
