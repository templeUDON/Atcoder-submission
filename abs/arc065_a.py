s = list(input())
n = len(s)
cnt = 0
word = ["d","r","e","a","m","e","r","a","s","e","r"]
s += "XXXXXXXXXXXXXXXX"

while True:
  if s[cnt] == "d":
    for i in range(1,5):
      if s[cnt+i] != word[i]:
        print("NO")
        exit()
    cnt += 5
    if s[cnt] == "e" and s[cnt+1] == "r" and s[cnt+2] == "a" and s[cnt+3] == "s" and s[cnt+4] == "e" and s[cnt+5] == "r":
      cnt += 6
    elif s[cnt] == "e" and s[cnt+1] == "r" and s[cnt+2] == "a" and s[cnt+3] == "s" and s[cnt+4] == "e":
      cnt += 5
    elif s[cnt] == "e" and s[cnt+1] == "r":
      cnt += 2
  elif s[cnt] == "e":
    for i in range(1,5):
      if s[cnt+i] != word[5+i]:
        print("NO")
        exit()
    cnt += 5
    if s[cnt] == "r":
      cnt += 1
  elif s[cnt] == "X":
    print("YES")
    exit()
  else:
    print("NO")
    exit()



