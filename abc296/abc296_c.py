n,x = list(map(int,input().split()))
a = list(map(int,input().split()))
b = set(a)

for i in range(n):
  tmp = a[i] - x
  if tmp in b:
    print("Yes")
    exit()
    
print("No")