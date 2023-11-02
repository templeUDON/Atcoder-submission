n = int(input())
a = list(map(int,input().split()))
all = {i+1 for i in range(n)}
called = set()

for i in range(n):
  if i+1 not in called:
    called.add(a[i])
    
ans = list(all - called)
print(len(ans))
print(*ans)
  