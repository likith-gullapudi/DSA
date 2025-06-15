
def fun(index,prev):
    if index==n:
        return 0
    temp = 10 ** 9
    if prev==0:
        if arr[index]>=arr[index-1]:
            temp= fun(index+1,0)
        if rev[index]>=arr[index-1]:
            temp=min(temp,fun(index+1,1)+cost[index])

        return temp
    else:
        if arr[index]>=rev[index-1]:
            temp= fun(index+1,0)
        if rev[index]>=rev[index-1]:
            temp=min(temp,fun(index+1,1)+cost[index])

        return temp


for _ in range(int(input())):
    n=int(input())
    cost=[int(x) for x in input().split()]
    arr=[]
    rev=[]
    dp = [[-1 for i in range(2)] for j in range(n + 1)]
    for index in range(n,-1,-1):
        for prev in range(2):
            if index==n:
                dp[index][prev]=0
                continue
            else:
                temp = 10 ** 9
                if prev == 0:
                    if arr[index] >= arr[index - 1]:
                        temp = fun(index + 1, 0)
                    if rev[index] >= arr[index - 1]:
                        temp = min(temp, fun(index + 1, 1) + cost[index])

                    dp[index][prev]=temp

                else:
                    if arr[index] >= rev[index - 1]:
                        temp = fun(index + 1, 0)
                    if rev[index] >= rev[index - 1]:
                        temp = min(temp, fun(index + 1, 1) + cost[index])

                    dp[index][prev]=temp


    for i in range(n):
        s=input()
        arr.append(s)
        rev.append(s[::-1])
    print(arr,rev)
    a=min(dp[1][1]+cost[0],dp[1][0])
    print(a)