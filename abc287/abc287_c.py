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


n,m = list(map(int,input().split()))
uf = UnionFind(n)
N = [0]*(n)
for i in range(m):
  u,v = list(map(int,input().split()))
  u -= 1
  v -= 1
  N[u] += 1
  N[v] += 1
  uf.union(u,v)

cnt = 0
for u in uf.parents:
  if u < 0:
    cnt += 1

for i in range(n):
  if N[i] >= 3:
    print("No")
    exit()

if cnt == 1 and n -m == 1: 
  print("Yes")
else:
  print("No")