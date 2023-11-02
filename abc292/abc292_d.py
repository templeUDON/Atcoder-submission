import sys
sys.setrecursionlimit(10**7)

def dfs(v):
  global vertex, edge
  
  done[v] = True
  vertex += 1
  edge += n_of_edge[v]
  for next_v in e[v]:
    if not done[next_v]:
      dfs(next_v)
  

n,m = list(map(int,input().split()))
e = [[] for _ in range(n+1)]
done = [False]*(n+1)
n_of_edge = [0]*(n+1)
v = []
for i in range(m):
  u,v = list(map(int,input().split()))
  e[u].append(v)
  e[v].append(u)
  n_of_edge[u] += 1 

result = True
for i in range(1,n+1):
  if not done[i]:
    vertex = 0
    edge = 0
    dfs(i)
    if vertex != edge:
      result = False

if result:
  print("Yes")
else:
  print("No")