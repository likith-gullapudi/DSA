import math

nums=[int(x) for x in input().split()]
bits=[0 for i in range(31)]
ans=0
prefix=[[0 for i in range(len(nums))] for i in range(32)]
for i in range(32):
    ones=zeros=0
    for index,num in enumerate(nums):
        #print(bin(1<<i),num&(1<<i))
        if (num&(1<<i)):
            prefix[i][index]+=1

        prefix[i][index]+=prefix[i][index-1] if index-1>=0 else 0
l,r=[int(x)-1 for x in input().split()]
xor=union=intersection=0
for i in range(32):
    ones = prefix[i][r] -(prefix[i][l-1] if l-1 >= 0 else 0)

    zeros=(r-l+1)-ones
    if ones<(r-l+1)//2:
        xor|=(1<<i)
    if ones<(r-l+1):
        union|=(1<<i)
    if ones>0:
        intersection|=(1<<i)
ans=xor+union+intersection
