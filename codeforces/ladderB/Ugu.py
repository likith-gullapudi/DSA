#https://codeforces.com/contest/1732/problem/B
for _ in range(int(input())):
    l=int(input())
    s=[int(x) for x in input()]
    inverted=0
    one_encountered=False
    ans=0
    for i in range(len(s)):
        if inverted:
            s[i]^=1

        if s[i]==0 and one_encountered:
            inverted^=1
            one_encountered=True
            ans+=1
        elif s[i]==1:
            one_encountered=True
    print(ans)




