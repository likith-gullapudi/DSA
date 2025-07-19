def compute_lis(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find max
    max_len = max(dp)
    idx = dp.index(max_len)

    # Reconstruct LIS
    lis = []
    while idx != -1:
        lis.append(arr[idx])
        idx = prev[idx]
    lis.reverse()
    return max_len, lis

# Main
n = int(input())
arr = list(map(int, input().split()))

best_len = 0
best_seq = []

for i in range(n):
    # Create new array without arr[i]
    temp = arr[:i] + arr[i+1:]
    length, subseq = compute_lis(temp)
    if length > best_len:
        best_len = length
        best_seq = subseq

# Also consider original LIS without removal
length, subseq = compute_lis(arr)
if length > best_len:
    best_len = length
    best_seq = subseq

print("Length:", best_len)
print("Subsequence:", best_seq)
