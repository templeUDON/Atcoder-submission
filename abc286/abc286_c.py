from collections import deque
n,a,b = list(map(int,input().split()))
s = list(input())
q = deque()
goukei = 0
for i in range(n):
  q.append(s[i])

cnt = 0
for i in range(n//2):
  if q[i] != q[-1-i]:
    cnt += 1

goukei = cnt * b

for i in range(1,n):
  q.append(q.popleft())
  cnt = 0
  for j in range(n//2):
    if q[j] != q[-1-j]:
      cnt += 1
  goukei = min(goukei,i*a+cnt*b)

print(goukei)