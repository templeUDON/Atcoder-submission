b = int(input())

cnt = 1
while True:
  if cnt**cnt == b:
    print(cnt)
    break
  elif cnt**cnt > b:
    print(-1)
    break
  else:
    cnt += 1