n,y = map(int,input().split())

for i in range(n+1):
  for j in range(n+1-i):
    goukei = i*10000 + j*5000 + 1000*(n-i-j)
    if goukei == y:
      print(i,j,n-i-j)
      exit()
      
print(-1,-1,-1)