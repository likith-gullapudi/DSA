n,k=[int(x) for x in input().split()]
x,a,b,c=[int(x) for x in input().split()]
xor=0
arr=[x]
s=x
for i in range(1,k):
    arr.append((a*arr[-1]+b)%c)
    s+=arr[-1]
xor^=s
for i in range(k,n):
    arr.append((a*arr[-1]+b)%c)
    s+=arr[-1]
    s-=arr[i-k]
    xor^=s
print(xor)



