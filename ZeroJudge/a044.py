# ZeroJudge a044: Planes overlapping in space
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a044

def line(n):
  if n == 1:
    return 2
  else:
    return line(n - 1) + n

def surface(n):
  if n == 1:
    return 2
  else:
    return surface(n -1) + line(n - 1)

while True:
  try:
    print(surface(int(input())))
  except:
    break # End of input
