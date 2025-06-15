for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]

    if k==4:
        temp = [(k - int(x) % k) % k for x in arr]
        a = min(temp)
        if len(arr)>=2:

            #making 2 numbers even
            temp=[x%2 for x in arr]
            if temp.count(0)==2:
                a=min(a,0)

            elif temp.count(0)==1:
                a=min(a,1)
            else:
                a=min(a,2)
        print(a)
        continue






    arr=[(k-int(x)%k)%k for x in arr]

    #print(arr,k)
    print(min(arr))