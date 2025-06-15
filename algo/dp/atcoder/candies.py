n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
dp=[[0 for i in range(k+1)] for j in range(n+1)]
prefix_sum=[]
prev=[0 for i in range(k+1)]
MOD=10**9+7
for index in range(n):
    curr = [0 for i in range(k + 1)]
    for temp in range(k+1):
        if index==0:
            curr[temp]=int(temp<=arr[0])
            continue
        else:
            curr[temp]=(prefix_sum[temp+1]-prefix_sum[max(0,temp-arr[index])] )%MOD  #sum(prev[temp-i] for i in range(arr[index]+1) if temp-i>=0)
    prev=curr[:]
    prefix_sum=[0 for i in range(len(prev)+1)]

    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = (prev[i - 1] + prefix_sum[i - 1])%MOD  # arr[i-1] present element(pre moved one step forward) pre[i-1]prefix sum for beloe element
    #print(curr)


print(prev[k])