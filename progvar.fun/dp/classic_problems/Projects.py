import bisect
from collections import defaultdict
import bisect

n = int(input())
projects = []

for _ in range(n):
    s, e, r = map(int, input().split())
    projects.append((s, e, r))

# Sort by end time
projects.sort(key=lambda x: x[1])
ends = [e for s, e, r in projects]

# DP[i] = max reward using first i projects
dp = [0] * (n + 1)

for i in range(1, n + 1):
    s, e, r = projects[i - 1]
    print(s,e,r)

    # Find last project that ends before start time s
    j = bisect.bisect_right(ends, s - 1)
    print(j)
    # dp[i] = max of skipping or taking this project
    dp[i] = max(dp[i - 1], dp[j] + r)

print(dp[n])


# n = int(input())
# projects_by_start = defaultdict(list)
# start_times = set()
#
# # Read and group projects by start time
# for _ in range(n):
#     s, e, r = map(int, input().split())
#     projects_by_start[s].append((e, r))
#     start_times.add(s)
#
# # Compress the start times
# sorted_starts = sorted(start_times)
# idx_map = {time: i for i, time in enumerate(sorted_starts)}
# dp = [0] * (len(sorted_starts) + 1)  # dp[i] = max reward starting at time sorted_starts[i]
#
# # Process from last start time to first
# for i in range(len(sorted_starts) - 1, -1, -1):
#     t = sorted_starts[i]
#     dp[i] = dp[i + 1]  # Case: skip all projects starting at time t
#
#     for e, r in projects_by_start[t]:
#         next_i = bisect.bisect_left(sorted_starts, e + 1)
#         if next_i < len(dp):
#             dp[i] = max(dp[i], r + dp[next_i])
#         else:
#             dp[i] = max(dp[i], r)  # Take only this project, no future one
#
# # Final answer is max reward starting from earliest possible time
# print(dp[0])

# dp=[0 for i in range(max_end+2)]
# for t in range(max_end+1,-1,-1):
#     #find next possible start
#     s_index=bisect.bisect_left(start_times,t)
#     if s_index==len(start_times):
#         continue
#     else:
#         s=start_times[s_index]
#     print(t,s)
#     if s>=max_end:
#         continue
#     else:
#         for e,r in p.get(s):
#             dp[t]=max(dp[t],r+dp[e+1])
# print(dp[0])



#

#     projects_by_start[s].append((e, r))
#     start_times_set.add(s)
#     start_times_set.add(e + 1)  # we might query dp[end + 1]
#
# # Coordinate compress time points
# sorted_times = sorted(start_times_set)
# time_to_idx = {t: i for i, t in enumerate(sorted_times)}
# dp = [0] * (len(sorted_times))
#
# # Process times in decreasing order
# for i in range(len(sorted_times) - 1, -1, -1):
#     t = sorted_times[i]
#     # Option 1: skip this time
#     dp[i] = dp[i + 1] if i + 1 < len(dp) else 0
#     # Option 2: take one or more projects starting at time t
#     for e, r in projects_by_start.get(t, []):
#         j = time_to_idx.get(e + 1, bisect.bisect_left(sorted_times, e + 1))
#         dp[i] = max(dp[i], r + (dp[j] if j < len(dp) else 0))
#
# # Answer is dp[0] (max reward from earliest time)
# print(dp[0])
