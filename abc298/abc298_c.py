n = int(input())
q = int(input())
query = []
for i in range(q):
  query.append(list(map(int,input().split())))

card_l = [[] for _ in range(2*10**5)]
card_s = [set() for _ in range(2*10**5)]
N = [[] for _ in range(n)]
for i in range(q):
  if query[i][0] == 1:
    N[query[i][2]-1].append(query[i][1])
    if query[i][2] not in card_s[query[i][1]-1]:
      card_l[query[i][1]-1].append(query[i][2])
      card_s[query[i][1]-1].add(query[i][2])
  elif query[i][0] == 2:
    N[query[i][1]-1].sort()
    print(*N[query[i][1]-1])
  else:
    card_l[query[i][1]-1].sort()
    print(*card_l[query[i][1]-1])
