n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

A = []
B = []
for i in range(n):
    A.append([a[i],0])
for i in range(m):
    B.append([b[i],1])
  
C = A + B
C.sort()
CA = []
CB = []
for i in range(len(C)):
  if C[i][1] == 0:
    CA.append([C[i],i+1])
  else:
    CB.append([C[i],i+1])

for i in range(n):
  print(CA[i][1], end = " ")
print("")
for i in range(m):
  print(CB[i][1], end = " ")