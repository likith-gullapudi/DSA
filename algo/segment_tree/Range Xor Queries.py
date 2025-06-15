n,q=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
prefix_xor=[arr[i] for i in range(n)]
prefix_xor.append(0)

for i in range(1,n):
    prefix_xor[i]^=prefix_xor[i-1]
#print(prefix_xor)
for _ in range(q):
    l,r=[int(x) for x in input().split()]
    print(prefix_xor[r-1]^prefix_xor[l-1-1])

