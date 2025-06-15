import sys, math
input = sys.stdin.readline

# ---------- DSU with parity (colour) and "blocked" flag ----------
class DSU:
    def __init__(self, n: int):
        self.par = list(range(n))       # parent
        self.sz  = [1] * n              # subtree size
        self.col = [0] * n              # parity w.r.t. parent (0 = same dir, 1 = opposite)
        self.bad = [False] * n          # True ⇒ component cannot rotate

    def find(self, x: int) -> int:
        if self.par[x] != x:
            p = self.par[x]
            self.par[x] = self.find(p)
            self.col[x] ^= self.col[p]   # path-compression plus parity update
        return self.par[x]

    # unite gears a and b (they must rotate in opposite directions)
    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)

        # already in same component
        if ra == rb:
            if self.col[a] == self.col[b]:        # same direction ⇒ odd cycle
                self.bad[ra] = True
            return

        # union by size (ra becomes the new root)
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
            a, b   = b, a

        # attach rb under ra
        self.par[rb] = ra
        # parity of rb w.r.t. new root so that a and b have opposite directions
        self.col[rb] = self.col[a] ^ self.col[b] ^ 1
        self.sz[ra] += self.sz[rb]
        self.bad[ra] |= self.bad[rb]

    # true if component containing x is blocked
    def blocked(self, x: int) -> bool:
        return self.bad[self.find(x)]

    # gears in same component?
    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    # parity between a and b (0 = same dir, 1 = opposite)
    def diff(self, a: int, b: int) -> int:
        self.find(a)
        self.find(b)
        return self.col[a] ^ self.col[b]


# ---------- main ----------
n, m = map(int, input().split())
teeth = list(map(int, input().split()))
dsu = DSU(n)

out_lines = []
for _ in range(m):
    q = list(map(int, input().split()))
    t = q[0]

    if t == 1:                              # change teeth
        x, c = q[1]-1, q[2]
        teeth[x] = c

    elif t == 2:                            # connect gears
        x, y = q[1]-1, q[2]-1
        dsu.union(x, y)

    else:                                   # query speed
        x, y, v = q[1]-1, q[2]-1, q[3]

        if not dsu.same(x, y) or dsu.blocked(x):
            out_lines.append("0")
            continue

        # direction
        sign = -1 if dsu.diff(x, y) else 1

        num = v * teeth[x] * sign
        den = teeth[y]
        g = math.gcd(abs(num), den)
        out_lines.append(f"{num // g}/{den // g}")

sys.stdout.write("\n".join(out_lines))
