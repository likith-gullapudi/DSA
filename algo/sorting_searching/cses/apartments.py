n,m,k=[int(x) for x in input().split()]
size=[int(x) for x in input().split()]
prefer=[int(x) for x in input().split()]
size.sort()
prefer.sort()
j=i=ans=0
while j<m and i<n:
    #print(size[i],prefer[j])
    if abs(size[i]-prefer[j])<=k:
        i+=1
        j+=1
        ans+=1
    elif size[i]>prefer[j]:
        j+=1
    else:
        i+=1
print(ans)