import math
N=300
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False


for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
primes=set()
for i in range(1,N):
    if is_prime[i]:
        primes.add(i)




def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def fun(n,a):
    #n=p+q
    # print(n)
    # print(primes)
    # print(n,a)
    if n in primes:
        print(2)
        print(a,n)
    else:
        print(3)
        for i in primes:
            # if i==2:
            #     print(i,n-j in primes)
            if n-i in primes:
                print(i,n-i,a)
                break





n=int(input())
if n in primes:
    print(1)
    print(n)
else:
    for i in range(n-2,1,-1):
        # print(i)
        if is_prime(i):

            fun(n-i,i)
            break