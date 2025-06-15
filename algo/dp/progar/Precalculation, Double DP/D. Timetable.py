
#lets optimze bottlneck finding minimum hours if we can skip k classes
#isnt it same as minimum hours if we attend total_classes-k classes
#(index,started,)

def fun(s):
    n = len(s)

    total_classes = sum([1 for i in range(n) if s[i] == '1'])
    # print(total_classes)
    hours = {}
    hours[0]=total_classes
    skips = {}

    for i in range(n):
        inbetween = 0
        for j in range(i, n):
            inbetween += 1 if s[j] == '1' else 0
            # print(i,j,inbetween)
            hours[(j - i + 1)] = min(hours.get(j - i + 1, float('inf')), total_classes - inbetween)
    for hour, skip in hours.items():
        if skip in skips:
            continue
        skips[skip] = hour
    #print(hours,skips)
    return skips


# fun("10110")
n, m, k = [int(x) for x in input().split()]
mn = []
for _ in range(n):
    s = input()
    mn.append(fun(s))

dp=[[-1 for _ in range(k+1)] for j in range(n)]
def fun(index, k):
    if index == n:
        return 0
    if dp[index][k]!=-1:
        return dp[index][k]
    ans = float('inf')
    for skip in range(m+1):
        if k - skip < 0:
            break
        ans = min(ans, fun(index + 1, k - skip) + mn[index].get(skip, 0))
    # print(index,k,ans)
    dp[index][k]=ans
    return ans


print(fun(0, k))
