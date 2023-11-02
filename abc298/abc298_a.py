n = int(input())
s = list(input())

ok = False
ng = False
for i in range(n):
  if s[i] == "o":
    ok = True
  elif s[i] == "x":
    ng = True
    
if ng == False and ok == True:
  print("Yes")
else:
  print("No")