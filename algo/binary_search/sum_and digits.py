def check(mid):
    digits = 0
    for i in str(mid):
        digits += int(i)
    return abs(digits - mid) >= s


for _ in range(int(input())):
    n, s = [int(x) for x in input().split()]
    lo, hi = 1, n
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid - 1

        else:
            ans = mid
            lo = mid + 1
    print(n - ans)