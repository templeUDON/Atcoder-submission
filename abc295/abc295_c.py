import collections
n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
cnt = 0
for v in c.values():
  cnt += v//2
  
print(cnt)