n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
t = 0
for i in range(m):
  t += a[b[i]-1]
  
print(t)