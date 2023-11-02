s = list(input())
t = list(input())

last = s[-len(t):]
flag = [True]*len(t)
cnt = 0
for i in range(len(t)):
  if last[i] != "?" and t[i] != "?" and last[i] != t[i]:
    flag[i] = False
    cnt += 1

if cnt == 0:
  print("Yes")
else:
  print("No")

for i in range(len(t)):
  last[i] = s[i]
  if last[i] != "?" and t[i] != "?" and last[i] != t[i]:
    if flag[i]:
      flag[i] = False
      cnt += 1
  else:
    if not flag[i]:
      flag[i] = True
      cnt -= 1
  
  if cnt == 0:
    print("Yes")
  else:
    print("No")