from collections import defaultdict


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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

n = int(input())
uf = UnionFind(2*n)

cnt = 0
g = set()
d = dict()
for _ in range(n):
    s,t = input().split()
    if s not in g:
      g.add(s)
      d[s] = cnt
      cnt += 1
    if t not in g:
      g.add(t)
      d[t] = cnt
      cnt += 1
    if uf.same(d[s],d[t]):
      print("No")
      exit()
    else:
      uf.union(d[s],d[t])

print("Yes")