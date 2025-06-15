#!/usr/bin/env python3
n = int(input())
if n%2 :
    print(0)
    exit()
ans = 0
n //= 2
while n > 0 :
    ans += n//5
    n //= 5
print(ans)