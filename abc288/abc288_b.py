n,k = list(map(int,input().split()))
s = []
for i in range(k):
  s.append(input()) 

s.sort()
for i in range(k):
  print(s[i])
