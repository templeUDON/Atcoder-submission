import bisect
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []
for i in range(n):
  dist = bisect.bisect_left(a, a[i]+m)-1
  ans.append(dist-i+1)
  
print(max(ans))

