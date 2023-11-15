import sys
sys.setrecursionlimit(10**7)

def dfs(c, x):
  global flag
  X[c] = x
  for i in g[c]:
    if X[i] == -1:
      dfs(i, 1-x) 
    elif X[i] == X[c]:
      flag = False

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

flag = True
X = [-1]*n

g = [[] for _ in range(n)]
for i in range(m):
  g[a[i]-1].append(b[i]-1)
  g[b[i]-1].append(a[i]-1)

for i in range(n):
  if X[i] == -1:
    dfs(i,0)

if flag:
  print("Yes")
else:
  print("No")
