N=10**6+20
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False


def perfect_square(n):
    lo,hi=1,n
    ans=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if mid**2>=n:
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    return ans**2==n and is_prime[ans]
_=int(input())
for n in [int(x) for x in input().split()]:
    if n==1:
        print('NO')
        continue
    if perfect_square(n):
        print('YES')
    else:
        print("NO")