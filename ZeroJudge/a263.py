# ZeroJudge a263: How many days ib between
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a263

import datetime # Somehow I found this tool

while True:
  try:
    input1 = [int(i) for i in input().split()]
    date1 = datetime.datetime(input1[0], input1[1], input1[2])
    input2 = [int(i) for i in input().split()]
    date2 = datetime.datetime(input2[0], input2[1], input2[2])
    print(abs((date1 - date2).days))
  except:
    break # End of input
