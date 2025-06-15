
l,r=[x for x in input().split()]
l='0'*(len(r)-len(l))+l
#print(l,r)
d={}
def fun(index,left_border,right_border,prev,val_started):
    if (index,left_border,right_border,prev) in d:
        return d[(index,left_border,right_border,prev) ]
    if index==len(r):
        return 1
    tlo=0
    if left_border:
        tlo=int(l[index])
    thi=9
    if right_border:
        thi=int(r[index])
    ans=0
    for i in range(tlo,thi+1):
        ntlo,nthi=left_border,right_border
        if (str(i)!=l[index]):ntlo=False
        if (str(i)!=r[index]):nthi=False
        if prev!=i or not val_started:

            ans+=fun(index+1,ntlo,nthi,i,val_started|(i!=0))
    d[(index, left_border, right_border, prev)]=ans
    return ans
print(fun(0,True,True,-1,False))



