for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        for i in range(n):
            print(n,end=" ")
    else:
        for i in range(n-2):
            print(4,end=" ")
        print("2"+" "+"6")
    print()