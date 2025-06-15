#first make series connections
import math

a,b=[int(x) for x in input().split()]
ans=a//b
a,b=a%b,b
#print(a,b)
if a!=0:
    gcd=math.gcd(a,b)
    a,b=a//gcd,b//gcd
    ans+=b
print(ans)
