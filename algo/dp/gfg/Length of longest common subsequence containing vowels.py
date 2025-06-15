x=input()
y=input()
dp=[[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
vowels=set(i for i in 'aeiou')
print('a' in vowels)
for i in range(len(x),-1,-1):
    for j in range(len(y),-1,-1):
        if i==len(x) or j==len(y):
            dp[i][j]=0
            continue
        else:
            #print(i, j, x[i], y[j], x[i] == y[j], x[i] not in vowels)
            if x[i]==y[j]:
                if x[i] not in vowels:
                    dp[i][j]=dp[i+1][j+1]
                    continue

                else:
                    dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i][j],dp[i+1][j],dp[i][j+1])

def printsol():
    i,j=0,0
    ans=''
    while i<len(x) and j<len(y):
        if x[i] == y[j]:
            if x[i] not in vowels:
                i+=1
                j+=1
                continue
            else:
                ans = ans + x[i]
                i+=1
                j+=1

        else:
            if dp[i+1][j]==dp[i][j]:
                i+=1
            else:
                j+=1
    print(ans)

print(dp[0][0])
printsol()
