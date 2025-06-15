class dsu:
    def __init__(self,arr):
        self.n = len(arr)
        self.parent = [i for i in range(self.n)]
        self.size = [1] * self.n
        self.s=[val for val in arr]
        self.added=[False for i in range(self.n)]
        self.max_sum=0

    def findpar(self, val):
        if self.parent[val] == val:
            return val
        self.parent[val] = self.findpar(self.parent[val])  # path compression
        return self.parent[val]

    def union(self, a, b, c=None):
        if c is not None:
            # If three arguments are given, handle accordingly
            self.added[b] = True
            self.max_sum=max(self.max_sum, self.s[b])
            if a!=-1 and self.added[a]:
                self.union(a, b)
            if c!=self.n and  self.added[c]:
                self.union(b, c)
            return

        # Else handle the classic union by size logic
        a_par = self.findpar(a)
        b_par = self.findpar(b)
        if a_par != b_par:
            if self.size[a_par] >= self.size[b_par]:
                self.parent[b_par] = a_par
                self.size[a_par] += self.size[b_par]
                self.s[a_par] += self.s[b_par]
                if self.s[a_par] >= self.max_sum:
                    self.max_sum = self.s[a_par]
            else:
                self.parent[a_par] = b_par
                self.size[b_par] += self.size[a_par]
                self.s[b_par] += self.s[a_par]
                if self.s[b_par] >= self.max_sum:
                    self.max_sum = self.s[b_par]

    def group_size(self, val):
        par = self.findpar(val)
        return self.size[par]
    def get_max_sum(self):
        return self.max_sum
n=int(input())
arr=[int(x) for x in input().split()]
order=[int(x) for x in input().split()]
ans=[0 for i in range(n)]
obj=dsu(arr)
for i in range(n-1,-1,-1):
    x=order[i]-1
    ans[i]=obj.get_max_sum()
    obj.union(x-1,x,x+1)
for i in ans:
    print(i)
