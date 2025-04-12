# ZeroJudge a147: Print it all
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a147

while True:
  try:
    n = int(input())
    if n != 0: # n should be greater than 0
      for i in range(1,n): 
        if i%7 != 0: 
          print(i, end = '')
        print('')
    else:
      break 
  except:
    break # End of input
