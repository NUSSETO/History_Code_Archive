# ZeroJudge c087: Pi
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=c087

import math

num_in_list = int(input()) # How many numbers in the list
while num_in_list != 0:
  mylist = []
  mypi = 0
  valid_comb = 0
  all_comb = math.comb(num_in_list, 2)

  # Appending numbers into the list
  for i in range(num_in_list):
    mylist.append(int(input()))

  # Check if coprime
  for i in range(num_in_list - 1):
    for j in range(i + 1, num_in_list):
      if math.gcd(mylist[i], mylist[j]) == 1:
        valid_comb += 1

  if valid_comb == 0:
    print('No estimate for this dataset.')
  else:
    mypi = math.sqrt((all_comb*6)/valid_comb)
    print(round(mypi, 6))

  num_in_list = int(input())
    
  
