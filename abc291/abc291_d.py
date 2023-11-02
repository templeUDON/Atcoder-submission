n = int(input())
card = []
for i in range(n):
  card.append(list(map(int,input().split())))
dp = [[0,0]  for _ in range(n)]
dp[0] = [1,1]
MOD = 998244353 

for i in range(1,n):
  if card[i][0] != card[i-1][0]:
    dp[i][0] += dp[i-1][0]
  if card[i][0] != card[i-1][1]:
    dp[i][0] += dp[i-1][1]
    
  if card[i][1] != card[i-1][0]:
    dp[i][1] += dp[i-1][0]
  if card[i][1] != card[i-1][1]:
    dp[i][1] += dp[i-1][1]
    
  dp[i][0] %= MOD
  dp[i][1] %= MOD

print(sum(dp[-1])%MOD)
