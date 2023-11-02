s = list(input())
ans = 0
cnt = 0

while cnt < len(s):
  if cnt + 1 < len(s) and s[cnt] == "0" and s[cnt+1] == "0":
    cnt += 2
    ans += 1
  else:
    cnt += 1
    ans += 1
  
print(ans)