class segment_tree:
    def __init__(self,arr,n):
        self.n=n
        self.tree=[0 for i in range(4*self.n+2)]
        self.arr=arr
        self.build(1, 0, self.n - 1)
    def build(self,n,l,r):

        if l==r:
            self.tree[n]=1 if self.arr[l]%2==0 else 0
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
            self.tree[n]=1 if val%2==0 else 0
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
n=int(input())
arr=[int(x) for x in input().split()]
q=int(input())
obj=segment_tree(arr,n)
#print(obj.tree)
for _ in range(q):
    op,ind,val=[int(x) for x in input().split()]

    if op==0:
        ind-=1
        obj.update(ind,val)

    elif op==1:
        ind-=1
        val-=1
        print(obj.range_query(ind,val))
    else:
        ind -= 1
        val -= 1
        print((val-ind+1)-obj.range_query(ind,val))




