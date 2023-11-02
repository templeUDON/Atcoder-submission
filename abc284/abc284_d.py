import math
t = int(input())

for i in range(t):
  n = int(input())

  cnt = 2
  while True:
    if n % (cnt**2) == 0:
      p = cnt
      q = n // (cnt**2)
      print(p,q)
      break
    elif n % cnt == 0:
      q = cnt
      p = int(math.sqrt(n//q))
      print(p,q)
      break
    else:
      if cnt == 2:
        cnt += 1
      else:
        cnt += 2