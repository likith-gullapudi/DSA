import math
m=10**9+7
for _ in range(int(input())):
    b,a=[int(x) for x in input().split()]
    print(math.comb(a+b-1,b)%m)