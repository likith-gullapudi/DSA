class dsu:
    def __init__(self,n):
        self.n=n
        self.size=[1 for i in range(n+1)]
        self.parent=[i for i in range(n+1)]
        self.max_component_size=1
        self.no_components=n
    def findPar(self,node):
        if self.parent[node]==node:
            return node
        else:
            par=self.findPar(self.parent[node])
            self.parent[node]=par
            return par
    def merge(self,a,b):
        a=self.findPar(a)
        b=self.findPar(b)
        if a==b:
            return 0
        else:
            if self.size[a]>self.size[b]:
                self.size[a]+=self.size[b]
                self.parent[b]=self.parent[a]
            else:
                self.size[b] += self.size[a]
                self.parent[a] = self.parent[b]
        self.max_component_size=max(self.max_component_size, self.size[b], self.size[a])
        self.no_components-=1
        return 1
    def noCompnenets(self):
        return self.no_components
    def maSize(self):

        return self.max_component_size