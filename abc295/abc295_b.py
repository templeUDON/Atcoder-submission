r,c = list(map(int,input().split()))
b = []
for i in range(r):
  b.append(list(input()))

bomb = []
for i in range(r):
  for j in range(c):
    if b[i][j].isdecimal():
      bomb.append([i,j,int(b[i][j])])

for k in range(len(bomb)):
  for i in range(r):
    for j in range(c):
      if abs(i - bomb[k][0]) + abs(j - bomb[k][1]) <= bomb[k][2]:
        b[i][j] = "."

for i in range(r):
  print(*b[i], sep ="")