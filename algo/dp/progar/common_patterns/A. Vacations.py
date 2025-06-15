# def max_no_rest_days(n, activities):
#     # Initialize DP array with a large negative value
#     dp = [[0] * 3 for _ in range(n + 1)]
#
#     # Iterate through the days
#     for i in range(1, n + 1):
#         # If Vasya rests on the i-th day
#         dp[i][0] = max(dp[i - 1])
#
#         # If Vasya participates in a contest
#         if activities[i - 1] == 1 or activities[i - 1] == 3:
#             dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + 1
#
#         # If Vasya goes to the gym
#         if activities[i - 1] == 2 or activities[i - 1] == 3:
#             dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + 1
#
#     # Calculate the result
#     max_activity_days = max(dp[n])
#     return n - max_activity_days
def max_no_rest_days(index, prev_day_activity):
    if index==n:
        return 0
    a=1+max_no_rest_days(index+1,0)
    for today_activity in can_do[activities[index]]:

        if prev_day_activity==today_activity:
            continue
        a=min(a,max_no_rest_days(index+1,today_activity))
    return a




# Example Usage
n = int(input())
activities = list(map(int, input().split()))
can_do=[[],[2],[1],[1,2]]
print(max_no_rest_days(0, -1))
