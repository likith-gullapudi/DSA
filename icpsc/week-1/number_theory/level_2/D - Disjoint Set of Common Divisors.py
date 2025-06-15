
import math

a, b = [int(x) for x in input().split()]
a, b = min(a, b), max(a, b)

a_factors = set()
a_factors.add(1)
i = 2
while i * i <= a:
    if a % i == 0:
        a_factors.add(i)
        while a % i == 0:
            a //= i
    i += 1
if a > 1:
    a_factors.add(a)

ans=0
for i in a_factors:
    if b%i==0:
        ans+=1
print(ans)

