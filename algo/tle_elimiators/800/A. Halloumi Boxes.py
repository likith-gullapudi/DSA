#https://codeforces.com/problemset/problem/1903/A
def is_sorted(arr):
    #print(arr)
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    if k==1:
        print('YES' if is_sorted(arr) else 'NO')
        continue
    print('YES')
