# ZeroJudge a054: ID letter verification
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a054

while True:
  try:
    mylist = []
    str = input() # Whole ID
    sum = 0
    
    for i in range(len(str) - 1):
      mylist.append(str[i])
    mylist.append(str[i + 1])

    for i in range(8):
      j = 8 - i
      sum += int(mylist[i])*j
    sum += int(mylist[8])

    dic = {0:'BNZ',1:'CIP',2:'DOQ',3:'ER',4:'FS',5:'GT',6:'HU',7:'JVX',8:'KLY',9:'AMW'}
    print(dic[sum%10]) 
    
  except:
    break # End of input
