import sys

for _ in range(int(sys.stdin.readline())):
    def check(x):
        total = 0
        numPainters = 1

        for i in arr:
            total += i

            if total > x:
                # for next count
                total = i
                numPainters += 1

        return numPainters <= l

    n, l = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    lo, hi = max(arr), sum(arr)
    ans=hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)
