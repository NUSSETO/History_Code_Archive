# ZeroJudge a040: Armstrong Number 
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a040

mylist = [] # store Armstrong Numbers
n ,m = map(int, input().split()) # Find all Armstrong Numbers between n and m with n < m

for i in range(n, m + 1):
  sum_of_power = 0
  for j in str(i):
    sum_of_power += int(j)**len(str(i))
  if sum_of_power == i:
    mylist.append(sum_of_power)
    
if mylist == []:
  print('None')
else:
  print(*mylist)
