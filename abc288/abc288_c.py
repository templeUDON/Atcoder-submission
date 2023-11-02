class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * (n)
        self.n = n
        self.rank = [0] * (n)

    def find(self, a):
        if self.parents[a] < 0:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            self.parents[b] += self.parents[a]
            self.parents[a] = b
        else:
            self.parents[a] += self.parents[b]
            self.parents[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

n,m = list(map(int,input().split()))
uf = UnionFind(n)
for i in range(m):
  a,b = list(map(int,input().split())) 
  a -= 1
  b -= 1
  uf.union(a,b)

cnt = 0
for u in uf.parents:
  if u < 0:
    cnt += 1
  
print(max(0,m-(n-cnt)))
  





