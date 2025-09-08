s = input()
n = len(s)
MOD=10**9+7
dp = [0 for i in range(n)]
prefix_sum = [0 for i in range(n)]  # prefix_sum[i] = dp[0] + dp[1] + ... + dp[i]
last_occurrence = {}  # stores the rightmost index of each character

for i in range(n):
    if i == 0:
        dp[i] = 1
        prefix_sum[i] = dp[i]
        last_occurrence[s[i]] = i
        continue

    # Get sum from 0 to i-2
    total_sum = prefix_sum[i - 2] if i >= 2 else 0
    total_sum%=MOD
    dp[i] = total_sum

    # If this character appeared before in range [0, i-2], subtract the prefix sum up to that point
    if s[i] in last_occurrence:
        last_pos = last_occurrence[s[i]]
        print("here",i,last_pos)
        if last_pos <= i - 2 and last_pos-2>=0:  # Only if it's in the valid range
            # We want dp[last_pos+1] + ... + dp[i-2]
            # = prefix_sum[i-2] - prefix_sum[last_pos]
            dp[i] = total_sum - prefix_sum[last_pos-2]
            dp[i]%=MOD
    else:
        # Character never appeared before AND s[i] != s[i-1]
        if s[i] != s[i - 1]:
            dp[i] += 1
            dp[i]%=MOD


    # Update prefix sum and last occurrence
    prefix_sum[i] = prefix_sum[i - 1] + dp[i]
    prefix_sum[i]%=MOD
    last_occurrence[s[i]] = i
    # print(i,dp[i],prefix_sum[i])
    print(i,dp[i],prefix_sum[i])

print(sum(dp)%MOD)

#abab
'''
a
b
aa 
bb 
ab


'''