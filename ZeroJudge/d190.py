# ZeroJudge d190: Age Sort
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=d190

while True:
  try:
    n = int(input()) # Don't really nedd it in this case
    mylist = list(map(int, input().split()))
    mylist.sort()
    print(*mylist)
  except:
    break # End of input
