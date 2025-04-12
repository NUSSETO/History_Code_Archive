# ZeroJudge a040: Armstrong Number 
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a040

mylist = [] # store Armstrong Numbers
n ,m = map(int, input().split()) # Find all Armstrong Numbers between n and m with n < m

for i in range(n, m + 1):
  x = 0
  for j in str(i):
    x += int(j)**len(str(i))
  if x == i:
    mylist.append(x)

if mylist == []:
  mylist.append('None')

print(*mylist)
