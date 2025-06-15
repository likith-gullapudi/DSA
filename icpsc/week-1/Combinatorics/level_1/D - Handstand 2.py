def first_digit(x):
    while x >= 10:
        x //= 10
    return x

def count_pairs(N):
    count = [[0] * 10 for _ in range(10)]

    for k in range(1, N + 1):
        i = first_digit(k)
        j = k % 10
        count[i][j] += 1

    result = 0
    for i in range(1, 10):  # first digit can't be 0
        for j in range(10):
            result += count[i][j] * count[j][i]

    return result

# Example usage
N = int(input())
print(count_pairs(N))
