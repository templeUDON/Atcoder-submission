n,k = list(map(int,input().split()))
s = list(input())
want = ["x"]*n
cnt = 0
for i in range(n):
  if s[i] == "o" and cnt < k:
    want[i] = "o"
    cnt += 1
    
print(*want,sep="")