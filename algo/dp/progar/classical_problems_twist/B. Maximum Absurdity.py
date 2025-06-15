n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
prefix_sum=[val for val in arr]
for i in range(1,len(arr)):
    prefix_sum[i]+=prefix_sum[i-1]
#print(prefix_sum)
#dp(index,op)-max(dp( index+k,op+1)+pre[index+k]-pre[index-1],dp(index+1,op))
#base case if index==n or op==2:return 0
dp=[[0 for j in range(3)] for i in range(len(arr)+1)]
taken=[[-1 for j in range(3)] for i in range(len(arr)+1)]
for i in range(len(arr),-1,-1):
    for op in range(3):
        if i==len(arr) or op==0:
            dp[i][op]=0
            taken[i][op]=0
            continue
        # not take
        dp[i][op] = dp[i + 1][op]
        taken[i][op]=1
        #take
        if i+k-1<=len(arr)-1:
            #print(i+k,len(dp))
            temp=dp[i][op]
            take= prefix_sum[i+k-1]-(prefix_sum[i-1] if i-1>=0 else 0) +dp[i+k][op-1]
            dp[i][op]=max(dp[i][op], take)
            if take>=temp:
                taken[i][op]=2

i,op=0,2

while taken[i][op]!=0:
    #print(i,op,taken[i][op],dp[i][op])
    if taken[i][op]==1:
        i+=1
    else:
        print(i+1,end=" ")
        i+=k
        op-=1



