# ZeroJudge e927: Odering string
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=e927

while True:
  try:
    mystring = input()
    mylist = []
    for i in range(len(mystring)):
      mylist.append(mystring[i])
      
    if mylist == []:
      break
      
    mylist.sort()
    for i in range(len(mystring)):
      print(mylist[i], end = '')
  except:
    break # End of input

# Better version
#try:
  #while True:
    #mystring = input()
    #if not mystring:
      #break
    #print(''.join(sorted(mystring)))
#except EOFError:
  #pass
