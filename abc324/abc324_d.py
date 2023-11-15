n = int(input())
s = list(input())
s.sort()
ans = 0
cnt = 0
while True:
  if cnt**2 > 10**n:
    break
  else:
    a = list(str(cnt**2))
    if len(a) < len(s):
      for i in range(len(s)-len(a)):
        a.append("0")
    a.sort()
    if a == s:
      ans += 1

  cnt += 1
    
print(ans)