start=[]
end=[]
n=int(input())
for _ in range(n):
    i,j=[int(x) for x in input().split()]
    start.append(i)
    end.append(j)
start.sort()
end.sort()
ans=customers=0
i=j=0
while j<n:
    if i<n and start[i]<=end[j]:
        i+=1
        customers+=1
        ans=max(ans,customers)
    else:
        j+=1
        customers-=1
    #print(i,j,ans)
print(ans)


