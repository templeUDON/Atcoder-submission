n,x = list(map(int,input().split()))

dp = [[0 for _ in range(x+1)] for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
  a,b = map(int,input().split())
  for j in range(x+1):
    if dp[i][j]:
      dp[i+1][j] = 1
    elif 0 <= j-a and 0 < dp[i+1][j-a] < b+1:
      dp[i+1][j] = dp[i+1][j-a] + 1

if dp[-1][-1]:
  print("Yes")
else:
  print("No")