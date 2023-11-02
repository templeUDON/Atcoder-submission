n = int(input())

ans = []
for i in range(60):
  for j in range(50):
    ans.append((2**i)*(3**j))
    
for i in range(len(ans)):
  if n == ans[i]:
    print("Yes")
    exit()
    
print("No")
  
