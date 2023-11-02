n = int(input())
money = 0
for i in range(n):
  money += 10000*(i+1)/n
  
print(money)