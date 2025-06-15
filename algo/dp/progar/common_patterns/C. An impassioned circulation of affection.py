def fun(letter,m):
    l,r=0,0
    used=ans=0
    while r<n:
        used+=1 if s[r]!=letter else 0
        r+=1
        while used>m:
            used-=1 if s[l]!=letter else 0
            l+=1
        ans = max(ans, (r - 1) - l + 1)
        #print(s[l:r],ans,used)

    return ans






n=int(input())
s=input()
ans=[[-1 for i in range(n+1)] for j in range(26)]
for i in range(26):
    letter=chr(ord('a')+i)
    #print(letter)
    for m in range(n+1):
        ans[i][m]=fun(letter,m)
for _ in range(int(input())):
    m,letter=[x for x in input().split()]
    m=int(m)
    letter=ord(letter)-ord('a')
    print(ans[letter][m])