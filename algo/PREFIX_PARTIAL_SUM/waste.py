a='bcbdedbdedebbeeeccbbdbdeebbdce'
word2='bcbdedbdedebbeeecbbbdbdeebbdce'
for val,(i,j) in enumerate(zip(a,word2)):
    if i!=j:
        print(i,j,val)
temp=[0 for i in range(26)]
temp2=[0 for i in range(26)]
for i in a:
    x=ord(i)-ord('a')
    print(i, x)

    temp[x]+=1
for i in word2:

    x = ord(i) - ord('a')
    temp2[x]+=1

print(temp)
print(temp2)
#[0, 10, 4, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


