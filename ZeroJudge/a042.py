# ZeroJudge a042: Circle overlapping on plane
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a042

def fun(n):
  if n == 1:
    return 2
  else:
    return fun(n - 1) + 2*(n - 1)

while True:
  try:
    print(fun(int(input())))
  except:
    break # End of input
