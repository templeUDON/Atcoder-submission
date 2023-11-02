s = input()

if len(s) != 8:
  print("No")
  exit()
  
if not s[0].isalpha() or not s[-1].isalpha():
  print("No")
  exit()

for i in range(1,len(s)-1):
  if s[i].isalpha():
    print("No")
    exit()
    
x = int(s[1:len(s)-1])
if 100000 <= x <= 999999:
  pass
else:
  print("No")
  exit()

print("Yes")
