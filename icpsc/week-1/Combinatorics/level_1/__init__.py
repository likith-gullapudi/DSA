def find_best_pair(a):
    n = len(a)
    max_a = max(a)
    target = max_a / 2

    best_j = None
    best_diff = float('inf')

    for aj in a:
        if aj >= max_a:
            continue
        diff = abs(aj - target)
        if diff < best_diff:
            best_diff = diff
            best_j = aj

    print(max_a,best_j)
n=int(input())
arr=[int(x) for x in input().split()]
find_best_pair(arr)