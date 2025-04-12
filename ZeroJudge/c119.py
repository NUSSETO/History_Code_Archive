# ZeroJudge c119: I love big numbers
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=c119

while True:
  try:
    n = int(input())
    fac = 1
    sum = 0

    # Factorial, or just import math and use math.factorial()
    for i in range(1, n+1):
      fac *= i

    # Sum up individual numbers
    while fac != 0:
      sum += fac%10
      fac //= 10

    print(sum)
    
  except:
    break # end of input
