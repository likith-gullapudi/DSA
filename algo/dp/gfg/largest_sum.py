from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        def fun(index, c):
            n = len(arr)

            ans = -float('inf')
            # Base cases
            prev = [0 for i in range(2)]
            prev[0] = arr[0]
            prev[1] = arr[0]
            ans = max(prev)

            for i in range(1, n):
                curr = [0 for i in range(2)]
                # continue #start new
                curr[0] = max(prev[0] + arr[i], arr[i])

                # can exclude
                curr[1] = max(prev[0], prev[1] + arr[i])
                # print(ans,max(dp[i]))
                ans = max(ans, max(curr))
                prev = curr[:]

            return ans

        return fun(n - 1, 1)

