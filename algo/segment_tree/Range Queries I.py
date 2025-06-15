class segment_tree:
    def __init__(self,arr,n):
        self.n=n
        self.tree=[0 for i in range(4*self.n+2)]
        self.arr=arr
    def build(self,n,l,r):

        if l==r:
            self.tree[n]=self.arr[l]
            #print(l,r,n)
            return
        self.build(2*n,l,(l+r)//2)
        self.build(2*n+1,(l+r)//2+1,r)

        self.tree[n]=self.tree[2*n]+self.tree[2*n+1]
    def update(self,n,l,r,ind,val):
        if ind<l or ind>r:
            return
        if l==r:
            self.tree[n]=val
            self.arr[ind]=val
            return
        self.update(2 * n, l, (l + r) // 2,ind,val)
        self.update(2 * n + 1, (l + r) // 2 + 1, r,ind,val )

        self.tree[n]=self.tree[2*n]+self.tree[2*n+1]
    def range_query(self,n,l,r,gl,gr):
        if gl<=l<=r<=gr:
            return self.tree[n]
        if gr<l or gl>r:
            return 0
        a=self.range_query(2 * n, l, (l + r) // 2,gl,gr)
        b=self.range_query(2 * n + 1, (l + r) // 2 + 1, r,gl,gr)

        return a+b





n,q=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
obj=segment_tree(arr,n)
obj.build(1,0,n-1)
for _ in range(q):
    op,i,x=[int(x) for x in input().split()]
    if op==1:
        obj.update(1,0,n-1,i-1,x)
    else:
        print(obj.range_query(1,0,n-1,i-1,x-1))
