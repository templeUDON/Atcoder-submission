n = int(input())
s = list(input())

if len(s) == 1:
  print("Yes")
  exit()

for i in range(n-1):
  if s[i] == "M" and s[i+1] == "M":
    print("No")
    exit()
  elif s[i] == "F" and s[i+1] == "F":
    print("No")
    exit()
  
print("Yes")