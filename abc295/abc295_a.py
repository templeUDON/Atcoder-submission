n = int(input())
w = input().split()
alp = ["and", "not", "that", "the", "you"]

for i in range(n):
  if w[i] in alp:
    print("Yes")
    exit()
    
print("No")
