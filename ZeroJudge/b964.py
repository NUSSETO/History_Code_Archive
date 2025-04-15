# ZeroJudge b964: Score Perfermence Indicator
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=b964

while True:
  try:
    num_student = int(input())
    list_score = list(map(int, input().split()))

    list_pass = [x for x in list_score if x >= 60]
    list_fail = [x for x in list_score if x < 60]

    print(*sorted(list_score))
    
    if list_fail != []:
      print(max(list_fail))
    else:
      print('Best case')
      
    if list_pass != []:
      print(min(list_pass))
    else:
      print('Worst case')
    
  except:
    break # End of input
