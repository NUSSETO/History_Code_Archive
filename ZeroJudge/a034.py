# ZeroJudge a034: Binary conversion
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a034

while True:
  try:
    n = int(input())
    n = format(n, 'b') #Convert to binary using built-in function
    print(n)
  except:
    break
  
