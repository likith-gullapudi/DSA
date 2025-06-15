for _ in range(int(input())):
    n,x=[int(x) for x in input().split()]
    nums=[int(x) for x in input().split()]
    nums.sort()
    i,j=0,len(nums)-1
    ans=0
    while i<j:
        if nums[i]+nums[j]>x:
            j-=1
        else:
            ans+=(j-i)*2
            i+=1
    print(ans)