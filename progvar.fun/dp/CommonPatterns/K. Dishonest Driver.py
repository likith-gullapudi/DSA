def solve():
    n = int(input())
    s = input()

    # For each starting position i, compute the smallest period for each length
    # This avoids recomputing LPS arrays for overlapping substrings
    periods = {}

    for i in range(n):
        # Build LPS array incrementally for all substrings starting at i
        current_lps = []

        for end in range(i, n):
            length = end - i + 1

            if length == 1:
                current_lps = [0]
                periods[(i, end)] = 1  # single character, period = 1
            else:
                # Extend the LPS array for the new character
                j = current_lps[-1] if current_lps else 0
                while j > 0 and s[end] != s[i + j]:
                    j = current_lps[j - 1]
                if s[end] == s[i + j]:
                    j += 1
                current_lps.append(j)

                # Calculate period
                period = length - j
                if period != length and length % period == 0:
                    periods[(i, end)] = period
                else:
                    periods[(i, end)] = length

    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1  # atomic path

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1

            # option 1: split
            for k in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])

            # option 2: repetition
            period = periods[(l, r)]
            if period < length:  # has repetition
                dp[l][r] = min(dp[l][r], dp[l][l + period - 1])

    print(dp[0][n - 1])


solve()