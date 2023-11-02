import itertools
n,m = map(int,input().split())
s = []
for i in range(n):
  s.append(list(input()))
ans = 0
player = [i for i in range(n)]
for v in itertools.permutations(player,2):
  flag = True
  for i in range(m):
    if s[v[0]][i] == "x" and s[v[1]][i] == "x":
      flag = False
      break
  if flag:
    ans += 1

print(ans//2)