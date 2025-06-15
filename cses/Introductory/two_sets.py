n=int(input())
#if it is even
#1 2 3 4 5 6 7 8
#if lenght%4==0 sure
#if length%4==3  then 1 2 3 4 5 6 7 sure
#if lenght%4==2 then 1 2 3 4 5 6 7 8 9
if n%4==0:
    print('YES')
    a,b=[],[]
    i=1
    while i<=n:
        # print(i)
        a.append(i)
        a.append(i+3)
        b.append(i+1)
        b.append(i+2)
        i+=4
    #print(a,b)
    print(len(a))
    for i in a:
        print(i,end=" ")
    print(len(b))
    for i in b:
        print(i,end=" ")
elif n%4==3:
    print('YES')
    a=[1,2]
    b=[3]
    i=4
    while i<=n:
        a.append(i)
        a.append(i+3)
        b.append(i+1)
        b.append(i+2)
        i+=4
    print(len(a))
    for i in a:
        print(i,end=" ")
    print(len(b))
    for i in b:
        print(i,end=" ")
else:
    print("NO")




