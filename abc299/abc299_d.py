n = int(input())

ok = 0
ng = n-1

while ng - ok > 1:
  mid = (ok + ng)//2
  
  print("?", mid+1)
  ans = int(input())
  
  if ans == 1:
    ng = mid
  else:
    ok = mid
  
print("!", ok+1)