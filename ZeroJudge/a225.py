# ZeroJudge a225: We love combination.
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a225

while True:
  try:
    n = int(input()) # Dno't really need it in this case
    mylist = list(map(int, input().split()))
    mylist.sort(key = lambda x:x%10, -(x//10)) # First, sort based on ones digit, then sort based on the rest of the number in a revresed manner
    print(*mylist)
  except:
    break # End of input
