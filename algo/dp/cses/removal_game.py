import sys
sys.setrecursionlimit(10**4)


def max_score(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    def solve(l, r):
        if l > r:
            return 0
        if dp[l][r] != -1:
            return dp[l][r]

        take_left = arr[l] + min(solve(l + 2, r), solve(l + 1, r - 1))
        take_right = arr[r] + min(solve(l + 1, r - 1), solve(l, r - 2))

        dp[l][r] = max(take_left, take_right)
        return dp[l][r]

    d={}
    def fun2(l,r):
        if (l,r) in d:
            return d[(l,r)]
        if l==r:
            return arr[l]
        ans=-float('inf')
        ans=max(ans,arr[l]-fun2(l+1,r),arr[r]-fun2(l,r-1))
        d[(l, r)]=ans
        return ans
    x_minus_y =fun2(0,n-1)
    x_plus_y=sum(arr)
    x=(x_plus_y+x_minus_y)//2
    print(x)



    #return solve(0, n - 1)


# Example usage
n=int(input())
arr =[int(x) for x in input().split()]
max_score(arr)  # Output: 8
