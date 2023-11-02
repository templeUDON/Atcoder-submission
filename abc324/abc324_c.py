n,t = input().split()
n = int(n)
ans = []
for i in range(n):
  s = input()
  if len(t) == len(s):
    if s == t:
      ans.append(i+1)
    else:
      cnt = 0
      for j in range(len(s)):
        if s[j] != t[j]:
          cnt += 1
      if cnt == 1:
        ans.append(i+1)
  elif len(t) == len(s)+1:
    cnt = 0
    for j in range(len(t)):
      if j == len(t)-1 and cnt == 0:
        ans.append(i+1)
        break
      if s[j-cnt] != t[j]:
        cnt += 1
      if cnt >= 2:
          break
    else:
      ans.append(i+1)
        
  elif len(t) == len(s)-1:
    cnt = 0
    for j in range(len(s)):
      if j == len(s)-1 and cnt == 0:
        ans.append(i+1)
        break
      if s[j] != t[j-cnt]:
        cnt += 1
      if cnt >= 2:
          break
    else:
      ans.append(i+1)

print(len(ans))
print(*ans)
