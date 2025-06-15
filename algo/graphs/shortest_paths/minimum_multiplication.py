# User function Template for python3

from typing import List


class Solution:

    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        dist = [float('inf') for i in range(end + 1)]

        def bfs(node):
            q = [(0, node)]
            while q:
                print(q)
                temp_dist, temp = q.pop(0)
                if temp == end:
                    return temp_dist
                if temp_dist > dist[temp]:
                    continue

                for i in arr:
                    nei = i * temp % 100000

                    if nei > end:
                        continue
                    if temp_dist + 1 < dist[nei]:
                        dist[nei] = temp_dist + 1
                        q.append((dist[nei], nei))
            return -1

        dist[start] = 0
        return bfs(start)

# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int, input().split()))
        obj = Solution()
        print(obj.minimumMultiplications(arr, start, end))