import heapq

INF = 1<<60

n,a,b,c = map(int,input().split())
d = []
for i in range(n):
  d.append(list(map(int,input().split())))

start = 0
goal = n-1
ds = [INF for _ in range(n)]
ds[start] = 0
q = [(0,start)]
while q:
  cd, cur = heapq.heappop(q)
  
  if cd > ds[cur]:
    continue
  for next in range(n):
    if next == cur:
      continue
    if ds[cur]+d[cur][next]*a < ds[next]:
      ds[next] = ds[cur]+d[cur][next]*a 
      heapq.heappush(q,(ds[next],next))

dt = [INF for _ in range(n)]
dt[goal] = 0
q = [(0,goal)]
while q:
  cd, cur = heapq.heappop(q)
  
  if cd > dt[cur]:
    continue
  for next in range(n):
    if next == cur:
      continue
    if dt[cur]+d[cur][next]*b+c < dt[next]:
      dt[next] = dt[cur]+d[cur][next]*b+c 
      heapq.heappush(q,(dt[next],next))

ans = INF
for i in range(n):
  ans = min(ans,ds[i]+dt[i])
  
print(ans)
