# ZeroJudge a015: Transpose matrix
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a015

while True:
  try:
    
    # Read matrix dimensions, with blank in between the numbers
    row, col = input().split() 
    row = int(row)
    col = int(col)

    org = [] #Original matrix
    ans = [[0]*row for i in range(col)] #Transposed matrix

    # Read the original matrix by rows
    for i in range(row):
      org = [*org, list(map(int, input().split()))]

    # Transpose
    for i in range(row):
      for j in range(col):
        ans[j][i] = org[i][j]

    # Print the transposed matrix
    for i in range(col):
      print(*ans[i])
      
  except EOFError:
    break
      
