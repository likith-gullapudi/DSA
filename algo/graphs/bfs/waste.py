class Solution:
    def findOrder(self, alien_dict, N, K):
        # creating graph
        graph = [[] for i in range(26)]
        indegree = [0 for i in range(26)]
        for i in range(1, len(alien_dict)):
            prev = alien_dict[i - 1]
            present = alien_dict[i]
            for j in range(min(len(prev), len(present))):
                if present[j] != prev[j]:
                    print(ord(prev[j]) - ord('a'))
                    graph[ord(prev[j]) - ord('a')].append(ord(present[j])-ord('a'))
                    indegree[ord(present[j]) - ord('a')] += 1
        print(graph)
        q = []
        ans = []
        for i in range(26):
            if graph[i] != [] and indegree[i] == 0:
                q.append(i)

        while q:
            temp = q.pop(0)
            print(temp,ord('a'))
            ans.append(chr(temp + ord('a')))
            for nei in graph[temp]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return ans
print(Solution().findOrder(['baa', 'abcd', 'abca', 'cab', 'cada'],0,0))
