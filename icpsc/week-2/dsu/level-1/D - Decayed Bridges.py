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

    def union(self, a, b,x):
        a_par = self.findpar(a)
        b_par = self.findpar(b)
        a_size,b_size=self.size[a_par],self.size[b_par]

        if a_par != b_par:
            x = x - a_size ** 2 - b_size ** 2 + (a_size + b_size) ** 2
            if self.size[a_par] >= self.size[b_par]:
                self.parent[b_par] = a_par
                self.size[a_par] += self.size[b_par]

            else:
                self.parent[a_par] = b_par
                self.size[b_par] += self.size[a_par]
        return x



    def group_size(self, val):
        par = self.findpar(val)
        return self.size[par]

n,m=[int(x) for x in input().split()]
bridges=[]

a,b,ans=n**2,n,[0 for i in range(m+1)]
obj=dsu(n)
for _ in range(m):
    bridges.append([int(x)-1 for x in input().split()])
ans[m]=b
for i in range(m-1,-1,-1):
    b=obj.union(bridges[i][0],bridges[i][1],b)
    ans[i]=b


for i in ans[1:]:
    print((a-i)//2)
