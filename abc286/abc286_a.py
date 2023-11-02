n,p,q,r,s = list(map(int,input().split()))
a = list(map(int,input().split()))
pq = a[p-1:q]
rs = a[r-1:s]

a[p-1:q] = rs
a[r-1:s] = pq

print(*a)
  
