import math

for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    temp=1
    for val in arr:
        if val==temp:
            temp+=1
    print(math.ceil((n-temp+1)/k))