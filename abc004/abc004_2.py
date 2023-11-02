import numpy as np
c = []
for i in range(4):
  c.append(list(input().split()))

c = np.array(c)
c = np.rot90(c,2)
c = list(c)

for i in range(4):
  print(*c[i])