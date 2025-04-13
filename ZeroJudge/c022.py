# ZeroJudge c022: Odd Sum
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=c022

iteration = int(input('How many datasets need to be processed?'))
for i in range(iteration):
  try:
    num_begin = int(input('Enter the beginning number:'))
    num_end = int(input('Enter the ending number:')) + 1
    odd_sum = 0

    # The following code can be replaced with: sum(j for j in range(num_begin, num_end) if j%2 == 1)
    if num_begin%2 == 0:
      for j in range(num_begin + 1, num_end, 2):
        odd_sum += j
    else:
      for j in range(num_begin, num_end, 2):
        odd_sum += j
        
    print('Case', i + 1, ':', odd_sum)
  except:
    break # End of input
