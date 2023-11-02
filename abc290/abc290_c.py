n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
a = set(a)
a = list(a)
a.sort()
num = [i for i in range(k)]
order = []
for i in range(min(k,len(a))):
  if a[i] == num[i]:
    order.append(a[i])
  else:
    break
  
if len(order) == 0:
  print(0)
elif len(order) < k:
  print(max(order)+1)
else:
  print(max(num)+1)