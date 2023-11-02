s = list(input())

start = []
box = [False]*26
for i in range(len(s)):
  if s[i] == "(":
    start.append(s[i])
    
  elif s[i] == ")":
    while True:
      x = start.pop()
      if x == "(":
        break
      else:
        box[ord(x)-97] = False
  else:
    start.append(s[i])
    if box[ord(s[i])-97] :
      print("No")
      exit()
    else:
      box[ord(s[i])-97] = True

print("Yes")