#  yentIra coding cheskora ante anime perlu pedthaventIra
import math
MOD=10**9+7
for _ in range(int(input())):
    n,m,k=[int(x) for x in input().split()]
    dividing=math.comb(n-1,k)%MOD
    print((dividing*m*pow(m-1,k,MOD))%MOD)