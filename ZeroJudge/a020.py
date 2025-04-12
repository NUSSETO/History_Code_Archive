# ZeroJudge a020: Verify ID numbers
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a020

while True:
  try:
    list = [] # Store individual characters
    str = input() # Input ID
    sum = 0

    # Split the string into characters
    for i in range(len(str) - 1):
      list.append(str[i])
    list.append(str[i + 1])

    # Weighted sum calculation
    for i in range(9):
      j = 8 - i
      sum = sum + int(list[i + 1])*j
    sum = sum + int(list[9]) # Add the last digit
    
    # First letter to code mapping
    dic = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13 , 'E' : 14, 'F' : 15, 'G' : 16, 'H' : 17, 'I' : 34, 'J': 18,'K' : 19, 'L' : 20, 'M' : 21, 'N' : 22, 'O' : 35,'P' : 23, 'Q' : 24, 'R' : 25, 'S' : 26, 'T' : 27,'U' : 28, 'V' : 29, 'W' : 32, 'X' : 30, 'Y' : 31,'Z' : 33}

    # Convert first letter to numeric form
    LetterScore = (dic[list[0]]%10)*9 + dic[list[0]]//10
    sum = sum + LetterScore

    # Print results
    if sum%10 == 0:
      print('Real')
    else:
      print('Fake')
      
  except:
    break # End of input
