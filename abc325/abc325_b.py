n = int(input())
wx = []
for i in range(n):
  wx.append(list(map(int,input().split())))

time = [0]*24
for i in range(len(time)):
  for j in range(n):
    now = wx[j][1]+i
    now = now % 24
    if 9 <= now and now+1 <= 18:
      time[i] += wx[j][0]
      
print(max(time))