n,q = map(int,input().split())
s = list(input())

rui = [0]*n
cnt = 0
for i in range(n-1):
  if s[i] == s[i+1]:
    cnt += 1
  rui[i+1] = cnt

for i in range(q):
  l,r = map(int,input().split())
  print(rui[r-1]-rui[l-1])