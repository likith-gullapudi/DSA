n = int(input())
arr = list(map(int, input().split()))
prefix = 0
count = {0: 1}
ans = 0

for val in arr:
    prefix = (prefix + val) % n
    ans += count.get(prefix, 0)
    count[prefix] = count.get(prefix, 0) + 1

print(ans)
