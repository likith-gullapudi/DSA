def solve_atcoder(s):
    n = len(s)
    MOD = 1000000007

    dp = [0] * n
    prefix_sum = [0] * n
    last_occurrence = {}

    for i in range(n):
        if i == 0:
            dp[i] = 1
            prefix_sum[i] = dp[i]
            last_occurrence[s[i]] = i
            continue

        # Get sum from 0 to i-2 (all positions we can extend from)
        total_sum = prefix_sum[i - 2] if i >= 2 else 0
        dp[i] = total_sum

        # If this character appeared before, we need to avoid counting duplicates
        if s[i] in last_occurrence:
            last_pos = last_occurrence[s[i]]
            if last_pos <= i - 2:  # Only if it's in the valid range (not adjacent)
                # Remove the contribution from positions 0 to last_pos
                dp[i] = (total_sum - prefix_sum[last_pos]) % MOD
        else:
            # Character never appeared before AND s[i] != s[i-1] (can form single char string)
            if s[i] != s[i - 1]:
                dp[i] = (dp[i] + 1) % MOD

        # Update prefix sum and last occurrence
        prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % MOD
        last_occurrence[s[i]] = i

    # Sum all dp values to get total distinct strings
    result = sum(dp) % MOD
    return result


# Test cases from the problem
test_cases = [
    ("abc", 4),  # Expected: 4 (a, b, c, ac)
    ("aa", 1),  # Expected: 1 (a)
    ("acba", 6),  # Expected: 6 (a, b, c, aa, ab, ca)
    ("chokudai", 54)  # Expected: 54
]

print("Testing AtCoder F - Substrings:")
print("=" * 40)

for test_input, expected in test_cases:
    result = solve_atcoder(test_input)
    status = "✅" if result == expected else "❌"
    print(f"{status} Input: '{test_input}' -> Got: {result}, Expected: {expected}")

print("=" * 40)