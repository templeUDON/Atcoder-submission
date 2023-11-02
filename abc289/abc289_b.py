n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

ans = []
cnt = 0
for i in range(1,n+1):
  if i not in a:
    ans.append(i)
    j = i - 1
    for k in range(cnt):
      ans.append(j)
      j -= 1
    cnt = 0
  else:
    cnt += 1
    
print(*ans)
