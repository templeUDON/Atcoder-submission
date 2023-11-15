h,w = map(int,input().split())
s = []
t = []

for i in range(2*h):
  if i < h:
    s.append(list((input())))
  else:
    t.append(list((input())))
    
S = []
T = []
for i in range(w):
  x = []
  y = []
  for j in range(h):
    x.append(s[j][i])
    y.append(t[j][i])
    
  S.append(x)
  T.append(y)

S.sort()
T.sort()

if S==T:
  print("Yes")
else:
  print("No")
