import sys
sys.setrecursionlimit(10**7)

def dfs(x,y):
  global ans
  if y >= h or  x >= w:
    return
  order.append(a[y][x])
  if y == h-1 and x == w-1:
    if len(order) == len(set(order)):
      ans += 1
    
  dfs(x+1,y)
  dfs(x,y+1)
  order.pop()


h,w = list(map(int,input().split()))
a = []
for i in range(h):
  a.append(list(map(int,input().split())))

order = []
ans = 0
dfs(0,0)
print(ans)