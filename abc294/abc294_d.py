n,q = list(map(int,input().split()))
event = []
for i in range(q):
  event.append(list(map(int,input().split())))

done = set()
mini = 1

for i in range(q):
  if event[i][0] == 1:
    pass
  elif event[i][0] == 2:
    done.add(event[i][1])
  else:
    while True:
      if mini not in done:
        print(mini)
        break
      else:
        mini += 1
  