for _ in range(int(input())):
    n = int(input())
    arr = [[max(1, index + 1 - int(val)), min(index + 1 + int(val), n)] for index, val in enumerate(input().split())]

    # for every starting point find ending max ending pouint
    d = {}
    for i, j in arr:
        d[i] = max(d.get(i, -1), j)
    arr = []
    for i, j in d.items():
        arr.append((i, j))

    prev = 0
    ans = 1
    # print(arr)
    for i in range(1, len(arr)):
        if arr[i][0] == arr[prev][0] and arr[i][1] >= arr[prev][1]:
            prev = i
            continue
        if arr[i][0] >= arr[prev][0] and arr[i][1] <= arr[prev][1]:
            continue
        else:
            prev = i
            ans += 1
    print(ans)

