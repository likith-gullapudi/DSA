n,k=[int(x) for x in input().split()]
x,a,b,c=[int(x) for x in input().split()]
xor=0
arr=[x]

temp=x
for i in range(1,k):
    arr.append((a*arr[-1]+b)%c)
    temp^=arr[-1]
xor^=temp
for i in range(k,n):
    arr.append((a*arr[-1]+b)%c)
    temp^=arr[-1]
    temp^=arr[i-k]
    xor^=temp
print(xor)



