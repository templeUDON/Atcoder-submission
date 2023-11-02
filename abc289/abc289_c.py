import itertools
n,m = list(map(int,input().split()))
c = []
a = []
for i in range(m):
  c.append(int(input()))
  a.append(list(map(int,input().split())))

all = set(i+1 for i in range(n))

def change_dimensions(list1):
    search = list1[0]
    result = []
    if  not isinstance(search, (int, str)):
        for i in list1:
            result += i
    else:
        return list1
    return change_dimensions(result)
s = 0
ans = 0
for i in range(1,m+1):
  for v in itertools.combinations(a,i):
    s += 1
    x = change_dimensions(v)
    x = set(x)
    if x == all:
      ans += 1
      
print(ans)