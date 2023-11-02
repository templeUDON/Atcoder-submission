h,w = list(map(int,input().split()))
a = []
for i in range(h):
  a.append(list(map(int,input().split())))
 
alp = [".","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

ans = [""]*h
for i in range(h):
  for j in range(w):
    ans[i] += alp[a[i][j]]

for i in range(h):
  print(*ans[i],sep="")
    