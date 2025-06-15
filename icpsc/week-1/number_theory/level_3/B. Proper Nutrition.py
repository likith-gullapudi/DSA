n=int(input())
a=int(input())
b=int(input())
temp=False
for x in range(0,n+1):
    if n<x*a:
        temp=True
        break

    if (n-x*a)%b==0 :
        print("YES")
        print(x,(n-x*a)//b)
        exit()
print("NO")