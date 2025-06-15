l='1'
r=input()
count=len(r)-len(l)
l='0'*count+'1'
MOD=10**9+7
n=len(r)
d=int(input())
#dp[digit][tlo][thi][sum]=dp[digit+1].....[(sum+digit)%D)]
#base cas
dp=[[[[0 for i in range(d)] for j in range(2)] for k in range(2)] for z in range(n+1)]
for digit in range(n,-1,-1):
    for su in range(d):
        for tlo in range(2):
            for thi in range(2):
                if digit==n:
                    dp[digit][tlo][thi][su]=1 if su==0 else 0
                    continue
                else:
                    lo = int(l[digit]) if tlo else 0
                    hi = int(r[digit]) if thi else 9
                    for k in range(lo,hi+1):
                        ntlo = tlo and (k == lo)
                        nthi = thi and (k == hi)
                        dp[digit][tlo][thi][su]+=dp[digit+1][ntlo][nthi][(su+k)%d]
                        dp[digit][tlo][thi][su]%=MOD

print(dp[0][1][1][0])
