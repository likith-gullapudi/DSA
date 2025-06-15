MOD=10**9+7
n=int(input())
s=input()
dp=[[0 for i in range(n+1)] for j in range(n+1)]

temp=[0 for i in range(n)]
temp[0]=1 if s[0]=='>' else 0
temp[1]=1 if s[0]=='<' else 0
prefix_sum=[0 for i in range(n+1)]
for i in range(1,n+1):
    prefix_sum[i]=prefix_sum[i-1]+temp[i-1]
for index in range(2,n):
    curr = [0 for i in range(n )]
    for present in range(index+1):
        if s[index-1]=='<':
            curr[present]=prefix_sum[present]-prefix_sum[0]

            # for prev in range(present):
            #     curr[present]+=temp[prev]
        else:
            curr[present]=prefix_sum[index+1]-prefix_sum[present]
            # for prev in range(present,index+1):
            #     curr[present]+=temp[prev]
            #     curr[present]%=MOD
        curr[present] %= MOD

    temp=curr[:]
    prefix_sum=[0 for i in range(n+1)]
    for i in range(1,n+1):
        prefix_sum[i]=prefix_sum[i-1]+temp[i-1]
        prefix_sum[i]%=MOD

print(sum(temp)%MOD)