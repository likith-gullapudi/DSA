def fun(index=0,pos=0):
    if index==n:
        return 1
    ans=0
    if pos==0:
        ans+=fun(index+1,1)#for taking zero
        ans+=fun(index+1,0)#for taking one
    elif pos==1:
        ans+=fun(index+1,2)#one
        ans+=fun(index+1,1)#zero
    elif pos==2:
        ans+=fun(index+1,0)#for taking one
        ans+=fun(index+1,3)#for taking zero
    elif pos==3:
        ans+=fun(index+1,0)#for raking one
    return ans
for _ in range(int(input())):
    n=int(input())
    print(fun())

