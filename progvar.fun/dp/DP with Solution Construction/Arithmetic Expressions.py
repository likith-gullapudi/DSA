n = int(input())
arr = list(map(int, input().split()))
#dp[index][s] we are at index "index" with sum "s"
#base case index==n if s==0 return true else False
dp=[[-1 for i in range(101)] for j in range(n+1)]
for index in range(n,-1,-1):
    for s in range(101):
        if index==n:
            dp[index][s]=3 if s==0 else -1
            continue
        if dp[index+1][(s+arr[index])%101]!=-1:
            dp[index][s]=0 #0 means plus
            continue
        elif dp[index+1][(s-arr[index])%101]!=-1:
            dp[index][s]=1
            continue
        elif index!=0 and dp[index+1][(s*arr[index])%101]!=-1:
            dp[index][s]=2
            continue
d = ["+", "-", "*"]
# print(dp[0][0])
index, s = 0, 0
while index<n:
    if index!=0:
        print(d[dp[index][s]],end="")
    print(arr[index], end="")


    # Calculate next s based on the operator used
    if dp[index][s] == 0:  # addition
        s = (s + arr[index]) % 101
    elif dp[index][s] == 1:  # subtraction
        s = (s - arr[index]) % 101
    elif dp[index][s] == 2:  # multiplication
        s = (s * arr[index ]) % 101


    index += 1
# print((((55+3+45)*33)*25)%101)





