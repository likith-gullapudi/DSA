s=input()
d={}
for i in s:
    d[i]=d.get(i,0)+1
ans=""
exception=""
for i,j in d.items():

    if j%2==1:
        if exception:
            print("NO SOLUTION")
            break
        else:
            exception=i
            ans=ans
    ans = ans + i * (j // 2)
else:
    print(ans+exception+ans[::-1])

