n=int(input())+1
arr=[int(x) for x in input().split()]+[0]
#basically to divide array into 3 parts
#note- breaking is before index
#dp[index][cuts] means we are just before index i and used cuts c and it returns max value from i to n using cuts alreadys
#base case- dp[n]=0 and dp[n][3]=float('inf')
# def fun(index,cuts):
#     if index==n:
#         return 0
#     if cuts==3:
#         return -float('inf')
#     ans=0
#     ans=fun(index,cuts+1)
#     if cuts==0 or cuts==2:
#         ans=max(ans,-arr[index]+fun(index+1,cuts))
#     else :
#         ans=max(ans,arr[index]+fun(index+1,cuts))
#     return ans
dp=[[-1 for i in range(3+1)] for j in range(n+1)]
for index in range(n,-1,-1):
    for cuts in range(3,-1,-1):
        if index == n:
            dp[index][cuts]= 0
            continue
        if cuts == 3:
            dp[index][cuts]=-float('inf')
            continue
        dp[index][cuts]=ans=dp[index][cuts+1]
        if cuts == 0 or cuts == 2:
            ans = max(ans, -arr[index] +dp[index+1][cuts])
        else:
            ans = max(ans, arr[index] + dp[index+1][cuts])
        dp[index][cuts]=max(ans,dp[index][cuts])




print(dp[0][0])

