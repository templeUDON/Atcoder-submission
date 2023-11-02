class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


n,m = map(int,input().split())
nf = UnionFind(n)

for i in range(m):
  u,v = map(int,input().split())
  nf.union(u-1,v-1)

ans = 0  
for i in nf.parents:
  if i < 0:
    ans += 1
    
print(ans)