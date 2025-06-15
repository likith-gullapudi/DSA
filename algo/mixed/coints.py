import heapq
import math


class Solution:
    def findKthSmallest(self, coins, k: int) -> int:
        x = max(coins)
        small = min(coins)
        heapq.heapify(coins)
        used = []
        for index, i in enumerate(coins):
            coins[index] = [i, i]

        while True:

            val, den = heapq.heappop(coins)
            print(val, den,used)
            if val>x:
                break
            while coins and coins[0][0]==val:
                print(coins)
                a,b=heapq.heappop(coins)
                heapq.heappush(coins,[a+b,b])
            heapq.heappush(coins,[val+den,den])
            used.append(val)

        print(used)
        n = len(used)

        set = math.ceil(k / n)
        prev_set_val = (set - 1) * used[-1]

        remain = ((k % n) - 1) % n  # for 0 indecing
        present_set_first_ele = 0

        if prev_set_val % small == 0:
            present_set_first_ele = prev_set_val + small
        else:
            present_set_first_ele = math.ceil(prev_set_val / small) * small
        print(prev_set_val, present_set_first_ele, remain)

        print(present_set_first_ele + used[remain] - used[0])

        return present_set_first_ele + used[remain] - used[0]
print(Solution().findKthSmallest([6,3],8))