n=int(input())
#  ....1001....
#n-3 length 2 times
#(i),(n-4-i) while n-4-i>=0
#first function is finding n string such that it doesnt has 00
dp=[[0 for i in range(2)] for index in range(n+1)]
for index in range(n+1):
    for present in range(2):
        if index==0:
            dp[index][present]=1
            continue
        else:
            if present==1:
                dp[index][present]=dp[index-1][1]+dp[index-1][0]
            else:
                dp[index][present] = dp[index - 1][1]

print(dp[n-1][0]+dp[n-1][1])
fans=[0]
def fun(s,n):
    if len(s)==n:
        if '00' not in s:
            fans[0]+=1
            return
    else:
        fun(s+'0',n)
        fun(s+'1',n)
print(fun('',n))
print(fans[0])
#another way is (index,prev) is telling that prev is 0 or 1
#so we can move to if prev==0 we can move to (index+1,1)
#else we can move to fun(index+1,0) and fun(index+1,1)
#base case is if index==n:return 1
#answer is fun(1,1)+fun(1,0)
dp=[[0 for prev in range(2)] for index in range(n+1)]
for index in range(n,-1,-1):
    for prev in range(2):
        if index==n:
            dp[index][prev]=1
            continue
        else:
            if prev==1:
                dp[index][prev]=dp[index+1][1]+dp[index+1][0]
            else:
                dp[index][prev] = dp[index + 1][1]

print(dp[1][1]+dp[1][0])
