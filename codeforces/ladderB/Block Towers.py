for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    temp=sorted(arr[1:])
    for i in temp:
        arr[0]+=i
