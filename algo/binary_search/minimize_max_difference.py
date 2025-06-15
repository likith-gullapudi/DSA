def check(mid):
    ans = 0
    for i in range(1, n):
        ans += (arr[i] - arr[i - 1]) // mid - 1
    # print(mid,ans)
    return ans <= k


for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    lo, hi = 1, arr[-1] + arr[0] + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        temp = check(mid)
        # print(lo,mid,hi,temp)
        if temp:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)
