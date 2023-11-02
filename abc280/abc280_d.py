import math
k = int(input())

for i in range(2,2*10**6):
  tmp = math.gcd(k,i)
  
  if tmp != 1:
    k = k // tmp
    if k == 1:
      print(i)
      exit()
      
print(k)