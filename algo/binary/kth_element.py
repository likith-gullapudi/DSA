import bisect
import sys

def check(x):
    temp = 0
    for i in range(len(arr1)):
        temp += bisect.bisect_right(arr2, x - arr1[i])
    return temp >= k

for _ in range(int(sys.stdin.readline())):
    n, m, k = map(int, sys.stdin.readline().split())
    if n <= m:
        arr1 = list(map(int, sys.stdin.readline().split()))
        arr2 = list(map(int, sys.stdin.readline().split()))
    else:
        arr2 = list(map(int, sys.stdin.readline().split()))
        arr1 = list(map(int, sys.stdin.readline().split()))
    arr1.sort()
    arr2.sort()

    lo, hi = arr1[0] + arr2[0], arr1[-1] + arr2[-1]
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2

        if check(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)
