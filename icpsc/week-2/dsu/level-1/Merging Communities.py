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
        if a_par != b_par:
            if self.size[a_par] >= self.size[b_par]:
                self.parent[b_par] = a_par
                self.size[a_par] += self.size[b_par]
            else:
                self.parent[a_par] = b_par
                self.size[b_par] += self.size[a_par]

    def group_size(self, val):
        par = self.findpar(val)
        return self.size[par]
n,q=[int(x) for x in input().split()]
obj=dsu(n)
for _ in range(q):
    query=[x for x in input().split()]
    if query[0]=='M':
        obj.union(int(query[1])-1,int(query[2])-1)
    else:
        print(obj.group_size(int(query[1])-1))

