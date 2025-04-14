# ZeroJudge a225: We love combination.
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a225

while True:
  try:
    n = int(input()) # Dno't really need it in this case
    mylist = list(map(int, input().split()))
    mylist.sort(key = lambda x:(x%10, -x//10)) # Sort by ones digit, then by reverse of tens+ digit
    print(*mylist)
  except:
    break # End of input
