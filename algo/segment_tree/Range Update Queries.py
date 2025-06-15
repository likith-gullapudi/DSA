class segment_tree:
    def __init__(self,arr,n):
        self.n=n
        self.tree=[0 for i in range(4*self.n+2)]
        self.arr=[0 for i in range(n+1)]
        self.build(1, 0, self.n - 1)
    def build(self,n,l,r):

        if l==r:
            self.tree[n]=self.arr[l]
            #print(l,r,n)
            return
        self.build(2*n,l,(l+r)//2)
        self.build(2*n+1,(l+r)//2+1,r)

        self.tree[n]=self.tree[2*n]+self.tree[2*n+1]

    def update(self, ind, val, n=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        #print(l, r)
        if ind<l or ind>r:
            return
        if l==r:
            #print("here")
            self.tree[n]+=val
            self.arr[ind]=val
            return
        self.update(ind,val,2 * n, l, (l + r)//2)
        self.update(ind,val,2 * n + 1, (l + r)//2 + 1, r )
        self.tree[n]=self.tree[2*n]+self.tree[2*n+1]
    def range_query(self,gl,gr,n=1,l=0,r=None):
        if r is None:
            r = self.n - 1
        if gl<=l<=r<=gr:
            return self.tree[n]
        if gr<l or gl>r:
            return 0
        a=self.range_query(gl,gr,2 * n, l, (l + r) // 2)
        b=self.range_query(gl,gr,2 * n + 1, (l + r) // 2 + 1, r)

        return a+b
n,q=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
obj=segment_tree(arr,n)
for _ in range(q):
    temp=[x for x in input().split()]
    if temp[0]=='1':
        w,a,b,u=[int(x) for x in temp]
        a-=1
        b-=1
        #print(obj.tree)
        obj.update(a,u)
        obj.update(b+1,-u)
        #print(obj.tree)
    else:

        w,k=[int(x) for x in temp]
        k-=1
        print(arr[k]+obj.range_query(0,k))



