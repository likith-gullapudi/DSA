while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1