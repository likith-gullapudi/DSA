import heapq
class dsu:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def findpar(self, val):
        if self.parent[val] == val:
            return val
        self.parent[val] = self.findpar(self.parent[val])  # path compression
        return self.parent[val]

    def union(self, a, b):
        a_par = self.findpar(a)
        b_par = self.findpar(b)
        a_size, b_size = self.size[a_par], self.size[b_par]
        if a_par != b_par:
            if self.size[a_par] >= self.size[b_par]:
                self.parent[b_par] = a_par
                self.size[a_par] += self.size[b_par]
            else:
                self.parent[a_par] = b_par
                self.size[b_par] += self.size[a_par]
        return a_size*b_size

    def group_size(self, val):
        par = self.findpar(val)
        return self.size[par]
n=int(input())
ans=0
h=[]
obj=dsu(n)
for _ in range(n-1):
    u,v,w=[int(x) for x in input().split()]
    u-=1
    v-=1
    heapq.heappush(h,(w,u,v))
while h:
    w,u,v=heapq.heappop(h)
    ans+=w*obj.union(u,v)
print(ans)

