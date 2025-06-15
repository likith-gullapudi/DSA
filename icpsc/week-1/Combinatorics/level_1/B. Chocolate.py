n=int(input())
arr=[int(x) for x in input().split()]
if arr.count(1)==0:
    print(0)
    exit()
ans=1
for i in range(n):
    if arr[i]==1:
        prev_one=1
        zeros=0
        for j in range(i+1,n):
            if arr[j]==0:

                zeros+=1
            else:
                # print(j,zeros)
                ans*=(zeros+1)
                zeros=0
        break
print(ans)

