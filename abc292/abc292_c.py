n = int(input())
num = [0 for _ in range(n+1)]
ans = 0

for a in range(1,n):
  for b in range(1,n//a+1):
    num[a*b] += 1

for v in range(1,n):
  ans += num[v]*num[n-v]

print(ans)