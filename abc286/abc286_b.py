n = int(input())
s = list(input())
ans = []
for i in range(n-1):
  if s[i] == "n" and s[i+1] == "a":
    ans.append("n")
    ans.append("y")
  else:
    ans.append(s[i])

ans.append(s[-1])
print(*ans,sep="")