import math


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        MOD = 10 ** 9 + 7
        y_count = defaultdict(int)

        for x, y in points:
            y_count[y] += 1

        valid = []
        for count in y_count.values():
            if count >= 2:
                valid.append(math.comb(count, 2))

        if len(valid) < 2:
            return 0

        ans = 0
        for i in range(len(valid)):
            for j in range(i + 1, len(valid)):
                ans += valid[i] * valid[j]
                ans %= MOD
        return ans
