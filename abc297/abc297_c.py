h,w = list(map(int,input().split()))
s = []
for i in range(h):
  s.append(list(input()))

for i in range(h):
  for j in range(w-1):
    if s[i][j] == "T" and s[i][j+1] == "T":
      s[i][j] = "P"
      s[i][j+1] = "C"
  print(*s[i], sep ="")
    