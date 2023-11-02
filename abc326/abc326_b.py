n = int(input())
N = [int(i) for i in list(str(n))]

while True:
  if N[0]*N[1] == N[2]:
    print(n)
    break
  else:
    n += 1
    N = [int(i) for i in list(str(n))]
    
  