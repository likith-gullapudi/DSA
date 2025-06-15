n = int(input())
primes = [True for _ in range(n + 1)]
primes[0] = primes[1] = False  # 0 and 1 are not prime

for i in range(2, int(n**0.5) + 1):
    if primes[i]:
        for j in range(i*i, n+1, i):
            primes[j] = False
ans=[]
for i in range(2,n+1):
    if primes[i]:
        temp=i

        while temp<=n:
            ans.append(temp)
            temp*=i
print(len(ans))
for i in ans:
    print(i,end=" ")


