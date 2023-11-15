n = int(input())
s = 0
g = 0
time = 0
for i in range(n):
  t = list(map(int,input().split()))
  if abs(t[1]-s) + abs(t[2]-g) == t[0] - time:
    time = t[0]
    s = t[1]
    g = t[2]
  elif abs(t[1]-s) + abs(t[2]-g) < t[0] - time:
    if ((t[0] - time) - abs(t[1]-s) + abs(t[2]-g)) % 2 == 0:
      time = t[0]
      s = t[1]
      g = t[2]
    else:
      print("No")
      exit()
  else:
    print("No")
    exit()
    
print("Yes")
  



