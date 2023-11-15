a = []
for i in range(9):
  a.append(list(map(int,input().split())))

num = {1,2,3,4,5,6,7,8,9}
flag1 = [[False]*9 for _ in range(9)]
flag2 = [[False]*9 for _ in range(9)]
flag3 = [[False]*9 for _ in range(9)]

for i in range(9):
  x = set()
  for j in range(9):
    x.add(a[i][j])
  if x != num:
    print("No")
    exit()

for i in range(9):
  x = set()
  for j in range(9):
    x.add(a[j][i])
  if x != num:
    print("No")
    exit()
    
x = set()
for i in range(3):
  for j in range(3):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(3,6):
  for j in range(3):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(6,9):
  for j in range(3):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(3):
  for j in range(3,6):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(3,6):
  for j in range(3,6):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(6,9):
  for j in range(3,6):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(3):
  for j in range(6,9):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(3,6):
  for j in range(6,9):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
x = set()
for i in range(6,9):
  for j in range(6,9):
    x.add(a[i][j])
if x != num:
  print("No")
  exit()
    
print("Yes")