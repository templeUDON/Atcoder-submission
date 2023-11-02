s = list(input())
memo = [0]*5 #BBRKR
for i in range(len(s)):
  if s[i] == "B" and memo[0] == 0:
    memo[0] = i+1
  elif s[i] == "B":
    memo[1] = i+1
  
  if s[i] == "R" and memo[2] == 0:
    memo[2] = i+1
  elif s[i] == "R":
    memo[4] = i+1
    
  if s[i] == "K":
    memo[3] = i+1
    
if (memo[0] % 2 != memo[1] % 2) and (memo[2] < memo[3] and memo[3] < memo[4]):
  print("Yes")
else:
  print("No")