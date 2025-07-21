n,m=[int(x) for x in input().split()]
#dp[i][mask] means from row i to n-1 where present row is like that mask
#dp[n]=0
#dp[n][mask]=
def generate_mask(index,mask,new_mask):
    if index==len(mask):
        return [new_mask]
    # print(mask)
    if mask[index]=='1':
        a=generate_mask(index+1,mask,new_mask+'0')
    else:
        a=generate_mask(index+1,mask,new_mask+'1')
        if index+1<n and mask[index+1]=='0':
            a=a+generate_mask(index+2,mask,new_mask+'00')
    return a
dp={}
def fun(c,mask):
    if (c,mask) in dp:
        return dp[(c,mask)]
    if c==m:
        return 1 if int(mask)==0 else 0
    new_masks=generate_mask(0,mask,'')
    # print(mask,new_masks)
    for new_mask in new_masks:
        dp[(c,mask)]=dp.get((c,mask),0)+fun(c+1,new_mask)
    return dp[(c,mask)]

print(fun(0,''.join(['0' for i in range(n)])))


