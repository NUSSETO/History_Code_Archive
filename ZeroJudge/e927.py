# ZeroJudge e927: Odering string
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=e927

while True:
  try:
    mylist = []
    mystring = input()
    for i in range(len(mystring)):
      mylist.append(mystring[i])
      
    if mylist == []:
      break
      
    mylist.sort()
    for i in range(len(mystring)):
      print(mylist[i], end = '')
  except:
    break # End of input
