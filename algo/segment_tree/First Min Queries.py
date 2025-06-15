class SegmentTree:
    def __init__(self, arr, n):
        self.n = n
        self.arr = arr
        self.arr.append(-float('inf'))
        self.tree = [0 for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def build(self, n, l, r):
        if l == r:
            self.tree[n] = l
            return
        mid = (l + r) // 2
        self.build(2 * n, l, mid)
        self.build(2 * n + 1, mid + 1, r)
        a, b = self.arr[self.tree[2 * n]], self.arr[self.tree[2 * n + 1]]
        self.tree[n] = self.tree[2 * n] if a >= b else self.tree[2 * n + 1]

    def update(self, ind, val, n=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ind < l or ind > r:
            return
        if l == r:
            self.tree[n] = l
            self.arr[ind] += val
            return
        mid = (l + r) // 2
        self.update(ind, val, 2 * n, l, mid)
        self.update(ind, val, 2 * n + 1, mid + 1, r)
        a, b = self.arr[self.tree[2 * n]], self.arr[self.tree[2 * n + 1]]
        self.tree[n] = self.tree[2 * n] if a >= b else self.tree[2 * n + 1]

    def range_query(self, gl, gr, n=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if gl > r or gr < l:
            return -1  # No valid index
        if gl <= l <= r <= gr:
            return self.tree[n]
        mid = (l + r) // 2
        left = self.range_query(gl, gr, 2 * n, l, mid)
        right = self.range_query(gl, gr, 2 * n + 1, mid + 1, r)
        if left == -1:
            return right
        if right == -1:
            return left
        return left if self.arr[left] >= self.arr[right] else right

    def find(self, val, n=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            return l if self.arr[self.tree[n]] >= val else self.n
        if self.arr[self.tree[2 * n]] >= val:
            return self.find(val, 2 * n, l, (l + r) // 2)
        else:
            return self.find(val, 2 * n + 1, (l + r) // 2 + 1, r)


# Sample input handling for testing
n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))
obj = SegmentTree(arr, n)

for q in queries:
    ans = obj.find(q, 1, 0, n - 1)
    if ans == n:
        print(0, end=" ")
    else:
        obj.update(ans, -q)
        print(ans, end=" ")
