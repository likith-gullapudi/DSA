n,m=[int(x) for x in input().split()]
#dp[i][mask] means from row i to n-1 where present row is like that mask
#dp[n]=0
#dp[n][mask]=
def generate_mask(index,mask,new_mask):

    if index==n:
        return [new_mask]
    # print(mask)
    if mask&(1<<index):
        a=generate_mask(index+1,mask,new_mask)
    else:
        a=generate_mask(index+1,mask,new_mask|(1<<index))
        if index+1<n and mask&(1<<(index+1))==0:
            a=a+generate_mask(index+2,mask,new_mask)
    return a
dp={}
def fun(c,mask):
    if (c,mask) in dp:
        return dp[(c,mask)]
    if c==m:
        return 1 if int(mask)==0 else 0
    new_masks=generate_mask(0,mask,0)
    # print(mask,new_masks)
    for new_mask in new_masks:
        dp[(c,mask)]=dp.get((c,mask),0)+fun(c+1,new_mask)
    return dp[(c,mask)]
dp=[[0 for i in range(1<<n)] for j in range(m+1)]
for c in range(m,-1,-1):
    for mask in range(1<<n):
        if c==m:
            dp[c][mask]=1 if mask==0 else 0
            continue
        new_masks=generate_mask(0,mask,0)
        for maskk in new_masks:
            dp[c][mask]+=dp[c+1][maskk]

print(dp[0][0])


