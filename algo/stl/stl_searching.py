import bisect
for _ in range(int(input())):
    n,q=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    for _ in range(q):
        ind,val=[int(x) for x in input().split()]
        if ind==1:
            temp=bisect.bisect_right(arr,val)

            if temp==len(arr):
                print(-1,end=" ")
            else:
                if temp>=1 and arr[temp-1]==val:
                    print(val,end=" ")
                else:
                    print(arr[temp])


        if ind==2:
            temp=bisect.bisect_right(arr,val)
            if temp==len(arr):
                print(-1,end=" ")
            else:
                print(arr[temp],end=" ")

        if ind==3:
            print(bisect.bisect_right(arr,val),end=" ")
        if ind==4:
            print(bisect.bisect_left(arr,val),end=" ")
    print()
