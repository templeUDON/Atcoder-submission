a,b = list(map(int,input().split()))
cnt = 0

while a != b:
  
  if a > b:
    t = (a-1)//b
    a -= b*t
  elif a < b:
    t = (b-1)//a
    b -= a*t
  cnt += t
  
print(cnt)