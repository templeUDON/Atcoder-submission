s = []
for i in range(8):
  s.append(list(input()))

ans = ""
alp = ["a","b","c","d","e","f","g","h"]
num = ["1","2","3","4","5","6","7","8"]
for i in range(8):
  for j in range(8):
    if s[i][j] == "*":
      ans += alp[j] + num[7-i]
      print(ans)