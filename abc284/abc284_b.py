n = int(input())

for i in range(n):
  t = int(input())
  a = list(map(int,input().split()))
  ans = 0
  for j in range(t):
    if a[j] % 2 == 1:
      ans +=1
  print(ans)