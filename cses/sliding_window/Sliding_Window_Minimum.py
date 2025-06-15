from collections import deque

n,k=[int(x) for x in input().split()]
x,a,b,c=[int(x) for x in input().split()]
xor=0
prev=x
q=deque()
q.append((x,0))

for i in range(1,k):
    present=(a*prev+b)%c
    while q and q[-1][0]>=present:
        q.pop()
    q.append((present,i))
    prev=present
xor^=q[0][0]
for i in range(k,n):
    present = (a * prev + b) % c
    while q and i-q[0][1]>=k:
        q.popleft()
    while q and q[-1][0]>=present:
        q.pop()
    q.append((present, i))
    prev = present
    xor^=q[0][0]
print(xor)


