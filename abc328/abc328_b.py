n = int(input())
d = list(map(int,input().split()))
ans = 0
num = []
for i in range(1,n+1):
  for j in range(1,d[i-1]+1):
    if i < 10 and (i==j or i*11==j):
      ans += 1
    elif i % 11 == 0 and (i==j or i==j*11):
      ans += 1
      
print(ans)
