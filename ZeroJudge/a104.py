# ZeroJudge a104: Ordering
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a104

while True:
  try:
    n = input() # How many numbers need to be ordered
    mylist = list(map(int, input().split())) # The numbers that need to be ordered
    mylist.sort()
    print(*mylist)
  except:
    break # end of input
