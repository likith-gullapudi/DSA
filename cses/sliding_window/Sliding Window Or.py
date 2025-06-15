n,k=[int(x) for x in input().split()]
x,a,b,c=[int(x) for x in input().split()]
xor=0
arr=[x]
bitwise=[[0 for i in range(32)] for j in range(n)]
prefix_bitwise=[[0 for i in range(32)] for j in range(n)]
count=[0 for i in range(32)]
present=[0 for i in range(32)]
temp=x
for j in range(32):
    bitwise[0][j] = 1 if (arr[-1] & (1 << j)) != 0 else 0
    count[j] += 1 if (arr[-1] & (1 << j)) != 0 else 0
for i in range(1,k):
    arr.append((a*arr[-1]+b)%c)
    for j in range(32):
        bitwise[i][j]+=1 if (arr[-1]&(1<<j))!=0 else 0
        count[j]+=bitwise[i][j]
ans=0
for j in range(32):
    if count[j]:
        ans |= (1 << j)
xor = ans
# for i in prefix_bitwise[:k]:
#     print(i)
# print(k-1,ans)
for i in range(k,n):
    ans=0
    arr.append((a*arr[-1]+b)%c)
    for j in range(32):
        bitwise[i][j]=1 if (arr[-1]&(1<<j))!=0 else 0
        count[j]+=bitwise[i][j]
    for j in range(32):
        count[j] -= bitwise[i - k][j]
        if count[j]:
            ans|=(1<<j)
    # print(i,ans)
    xor^=ans



print(xor)



