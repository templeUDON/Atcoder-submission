from collections import deque 
h,w = list(map(int,input().split()))
s = []
for i in range(h):
  s.append(list(input()))

q = deque()
ans = 0
flag = [[True]*w for _ in range(h)]
for i in range(h):
  for j in range(w):
    if s[i][j] == "#" and flag[i][j]:
      q.append([i,j])
      ans += 1
      while q:
        for k in range(-1,2):
          for l in range(-1,2):
            if q[0][0]+k >= 0 and q[0][0]+k < h and q[0][1]+l >= 0 and q[0][1]+l < w:
              if s[q[0][0]+k][q[0][1]+l] == "#" and flag[q[0][0]+k][q[0][1]+l]:
                flag[q[0][0]+k][q[0][1]+l] = False
                q.append([q[0][0]+k,q[0][1]+l])
        q.popleft()  
            
print(ans)