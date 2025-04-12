# ZeroJudge d478: Common numbers - Easy version
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=d478

# each datasets contains two sets of numbers
n, m = map(int, input().split()) # n = how many datasets nedd to be processed, m = each datasets contains how many numbers whithin each sets

for i in range(n):
  a = set(map(int, input().split()))
  b = set(map(int, input().split()))
  c = a.intersection(b)
  print(len(c)) # How many numbers are in common
