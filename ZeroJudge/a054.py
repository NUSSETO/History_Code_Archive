# ZeroJudge a054: ID letter verification
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a054

while True:
  try:
    mylist = []
    ID_Number = input() # Whole ID
    Total = 0
    
    for i in range(len(ID_Number) - 1):
      mylist.append(ID_Number[i])
    mylist.append(ID_Number[i + 1])

    for i in range(8):
      j = 8 - i
      Total += int(mylist[i])*j
    Total += int(mylist[8])

    mydict = {0:'BNZ',1:'CIP',2:'DOQ',3:'ER',4:'FS',5:'GT',6:'HU',7:'JVX',8:'KLY',9:'AMW'}
    print(mydict[Total%10]) 
    
  except:
    break # End of input
