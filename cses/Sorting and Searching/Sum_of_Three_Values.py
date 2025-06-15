n,k=[int(x) for x in input().split()]
arr=[(int(x),index+1) for index,x in enumerate(input().split())]
arr.sort()
for i in range(n):
    l,r=i+1,n-1
    breaked=False
    while l<r:
        if arr[i][0]+arr[l][0]+arr[r][0]==k:
            print(arr[i][1],arr[l][1],arr[r][1])
            breaked=True
            break
        elif arr[i][0]+arr[l][0]+arr[r][0]<k:
            l+=1
        else:
            r-=1
    if breaked:
        break
else:
    print("IMPOSSIBLE")