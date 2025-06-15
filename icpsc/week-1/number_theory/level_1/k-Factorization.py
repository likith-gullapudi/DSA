N,k=[int(x) for x in input().split()]
import math

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False


for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
primes=[]
for i in range(1,N):
    if is_prime[i]:
        primes.append(i)
temp=0
ans=[]
if len(ans) == k - 1 and N != 1:
    for i in ans:
        print(i, end=" ")
    print(N)
else:
    while N:
        if temp==len(primes):
            print(-1)
            break
        if N%primes[temp]==0:
            N//=primes[temp]
            ans.append(primes[temp])
        else:
            temp+=1
        if len(ans)==k-1 and N!=1:
            for i in ans:
                print(i,end=" ")
            print(N)
            break


