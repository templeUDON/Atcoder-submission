l,n1,n2 = list(map(int,input().split()))
v1 = []
v2 = []
for i in range(n1+n2):
  if i < n1:
    v1.append(list(map(int,input().split())))
  else:
    v2.append(list(map(int,input().split())))

ans = 0
c_v1 = 0
c_v2 = 0
while True:
  if v1[c_v1][1] == v2[c_v2][1]:
    if v1[c_v1][0] == v2[c_v2][0]:
      ans += v1[c_v1][1]
    if c_v1 + 1 == n1:
      break
    c_v1 += 1
    c_v2 += 1
  elif v1[c_v1][1] > v2[c_v2][1]:
    if v1[c_v1][0] == v2[c_v2][0]:
      ans += v2[c_v2][1]
    v1[c_v1][1] -= v2[c_v2][1]
    c_v2 += 1
  else:
    if v1[c_v1][0] == v2[c_v2][0]:
      ans += v1[c_v1][1]
    v2[c_v2][1] -= v1[c_v1][1]
    c_v1 += 1
  
print(ans)
  
