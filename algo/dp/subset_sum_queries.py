# User function Template for python3

class Solution:
    def all_longest_common_subsequences(self, s, t):
        dp = [[-1 for i in range(len(t))] for j in range(len(s))]
        n,m=len(s),len(t)
        def fun(i, j):
            if i == len(s) or j == len(t):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            ans = -float('inf')
            if s[i] == t[j]:
                ans = max(ans, 1 + fun(i + 1, j + 1))
            else:
                ans = max(ans, fun(i + 1, j), fun(i, j + 1))
            dp[i][j] = ans
            return ans

        fun(0, 0)

        for i in range(n):
            for j in range(m):
                print(fun(i,j),end=" ")
            print()
        fans = set()

        def printsol(i, j, temp):
            if i == len(s) or j == len(t):
                fans.add(temp)
                return


            if s[i]==t[j]:
                printsol(i + 1, j + 1, temp + s[i])

            if fun(i, j) == fun(i + 1, j):
                printsol(i + 1, j, temp)
            if fun(i, j) == fun(i, j + 1):
                printsol(i, j + 1, temp)

        printsol(0, 0, "")
        return sorted(fans)
#abaabaaaaa aabbaaaaaabb


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.all_longest_common_subsequences(s, t)
        for i in ans:
            print(i, end=" ")
        print()
