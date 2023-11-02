n = int(input())
a = list(map(int,input().split()))  
m = int(input())
b = set(map(int,input().split()))
x = int(input())
step = set()
step.add(0)
for i in range(1,x+1):
  if i in b:
    pass
  else:
    for j in range(n):
      if i - a[j] in step:
        step.add(i)

if x in step:
  print("Yes")
else:
  print("No")