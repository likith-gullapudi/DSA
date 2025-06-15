for _ in range(int(input())):
    n=int(input())
    st=input()
    s=set()
    for i in range(1,len(st)):
        if st[i:i+2] in s:
            print('YES')
            break
        s.add(st[i-1:i+1])
    else:
        print('NO')

