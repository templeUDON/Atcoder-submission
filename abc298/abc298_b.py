import numpy as np

n = int(input())
a = []
b = []
for i in range(2*n):
  if i < n:
    a.append(list(map(int,input().split())))
  else:
    b.append(list(map(int,input().split())))

one = 0
for i in range(n):
  for j in range(n):
    if a[i][j] == 1:
      one += 1

a = np.array(a)
b = np.array(b)
for _ in range(4):
  cnt = 0
  a = np.rot90(a)
  for i in range(n):
    for j in range(n):
      if a[i][j] == 1 and b[i][j] == 1:
        cnt += 1
  if cnt == one:
    print("Yes")
    exit()
  
print("No")