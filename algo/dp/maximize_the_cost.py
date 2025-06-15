from collections import defaultdict
from functools import lru_cache

@lru_cache(None)
def rec(index, used, prev):
    if index == len(s) or used == k:
        return 0
    ans = 0
    for i in range(26):
        present_letter = chr(ord('a') + i)
        ans = max(ans, d[prev + present_letter] + rec(index + 1, used + int(present_letter != s[index]), present_letter))
    return ans

for _ in range(1):
    s, k = input().split()
    k = int(k)

    d = defaultdict(int)

    for _ in range(int(input())):
        x, y, cost = input().split()
        d[x + y] = int(cost)

    # Clear the cache before processing each test case
    rec.cache_clear()
    print(rec(0, 0, "@"))
