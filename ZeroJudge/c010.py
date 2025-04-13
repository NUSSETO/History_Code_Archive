# ZeroJudge c010: What is the Median?
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=c010

mylist = []

while True:
  try:
    number = int(input())
    mylist = [*mylist, num]
    mylist.sort()
    list_length = len(mylist)
    if list_length%2 == 1:
      print(mylist[(list_length - 1)//2])
    else:
      median_sum = mylist[list_length//2] + mylist[list_length//2 - 1]
      print(median_sum//2)
  except:
    break # End of input
