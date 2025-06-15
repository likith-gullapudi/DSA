def n_square_sum(n):
    return (n*(n+1)*(2*n+1))//6

def n_sum(n):
    return (n*(n+1))//2
mod=10**9+7
for _ in range(int(input())):
    n=int(input())
    ans=2*n_square_sum(n)-n_sum(n)
    # print(ans)
    print((ans*2022)%mod)
