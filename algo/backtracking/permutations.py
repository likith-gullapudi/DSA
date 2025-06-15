from collections import OrderedDict

n, a = map(int, input().split())
d = OrderedDict()
k = 0
temp = []


def rec():
    global k
    # base case
    if len(temp) == n:
        k += 1
        if k == a:
            if changed:
                print(" ".join([str(i) for i in range(1,x-13+1)]),end=" ")
            print(*temp)
            return True
        return False

    # choices
    for i, j in d.items():
        if j > 0:
            temp.append(i)
            d[i] -= 1
            if rec():
                return True
            d[i] += 1
            temp.pop()
    return False


# faster input
# No need to use in Python

if n>13:
    changed=True
    for i in range(n-13+1,n+1):
        d[i]=1
    x,n=n,13
else:
    changed=False
    for i in range(1, n + 1):
        d[i] = 1

rec()
