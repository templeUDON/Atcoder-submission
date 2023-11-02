n,q = list(map(int,input().split()))
event = []
for i in range(q):
  event.append(list(map(int,input().split())))
player = [0]*n

for i in range(q):
  if event[i][0] == 1:
    player[event[i][1]-1] += 1
  elif event[i][0] == 2:
    player[event[i][1]-1] += 2
  else:
    if player[event[i][1]-1] >= 2:
      print("Yes")
    else:
      print("No")