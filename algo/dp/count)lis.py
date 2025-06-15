def fun(index):
    if index==0:
        return [1,1]
    max_len=1
    if lis_lenght[index]!=-1 and no_of_lis[index]!=-1:
        return [lis_lenght[index],no_of_lis[index]]
    lis_lenght[index]=no_of_lis[index]=1
    for i in range(index):
        prev_lis_lenght,prev_no_of_lis=fun(i)
        if nums[index]>nums[i]:
            if prev_lis_lenght+1>max_len:
                max_len=lis_lenght[index]=prev_lis_lenght+1
                no_of_lis[index]=prev_no_of_lis

            elif lis_lenght[i]+1==max_len:

                no_of_lis[index]+=prev_no_of_lis

    return [lis_lenght[index],no_of_lis[index]]
for _ in range(int(input())):
    n=int(input())
    nums=[int(x) for x in input().split()]
    no_of_lis=[-1 for i in range(n)]
    lis_lenght=[-1 for i in range(n)]
    print(fun(n - 1))
    print( lis_lenght,no_of_lis)
    # no_of_lis[0]=1
    # lis_lenght[0]=1
    #
    # for index in range(1,len(nums)):
    #     max_len=1
    #     for i in range(index):
    #         if nums[index]>nums[i]:
    #
    #             if lis_lenght[i]+1>max_len:
    #                 max_len=lis_lenght[index]=lis_lenght[i]+1
    #                 no_of_lis[index]=no_of_lis[i]
    #
    #             elif lis_lenght[i]+1==max_len:
    #
    #                 no_of_lis[index]+=no_of_lis[i]
    # m=max(lis_lenght)
    # #print(m,lis_lenght,no_of_lis)
    # ans=0
    # for index,i in enumerate(lis_lenght):
    #     if i==m:
    #         ans+=no_of_lis[index]
    # print(ans)



