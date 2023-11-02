n = int(input())
s = list(map(int,input().split()))
N = 5*n
s.sort()
p = []
for i in range(N):
  if i >= n and i < 4*n:
    p.append(s[i])
  
print(sum(p)/(3*n))