n,m = list(map(int,input().split()))
s = []
t = []
for i in range(n):
  s.append(list(input()))
for i in range(m):
  t.append(list(input()))
  
ans = 0
for i in range(n):
  for j in range(m):
    if s[i][3] == t[j][0] and s[i][4] == t[j][1] and s[i][5] == t[j][2]:
      ans += 1
      break
    
print(ans)