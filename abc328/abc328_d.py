s = list(input())

ans = []

for i in range(len(s)):
  ans.append(s[i])
  if len(ans) >= 3 and ans[-3] == "A" and ans[-2] == "B" and ans[-1] == "C":
    ans.pop()
    ans.pop()
    ans.pop()
  
print(*ans,sep="")