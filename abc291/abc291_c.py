n = int(input())
s = list(input())
x = 0
y = 0
memo = {(0,0)}
for i in range(n):
  if s[i] == "R":
    x += 1
  elif s[i] == "L":
    x -= 1
  elif s[i] == "U":
    y += 1
  else:
    y -= 1
  
  if (x,y) not in memo:
    memo.add((x,y))
  else:
    print("Yes")
    exit()

print("No")