# ZeroJudge a528: Ordering big numbers
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a528

while True:
  try:
    n = int(input()) # How many numbers to be ordered
    mylist = []

    for i in range(n):
      mylist.append(int(input())) # Input numbers that need to be ordered
    mylist.sort()
    
    for i in range(n):
      print(mylist[i])
    
  except:
    break # end of input
