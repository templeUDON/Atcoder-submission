n,t = map(int,input().split())
a = list(map(int,input().split()))

ans = t%sum(a)

for i in range(n):
  if a[i] < ans:
    ans -= a[i]
  else:
    break
  
print(i+1,ans)