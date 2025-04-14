# ZeroJudge e272: G.C.D of Fibonacci
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=e272

import math

# Fibonacci Function
def fib(n):
  p = 1
  q = 1
  sum_of_pq = 1
  if 3 <= n:
    for i in range(2,n):
      sum_of_pq = p + q
      q = p
      p = sum_of_pq
  return sum_of_pq

while True:
  try:
    a, b = map(int, input().split())
    print(fib(math.gcd(a, b))) # gcd(F(m),F(n))=F(gcd(m,n))
  except:
    break # End of input
