# ZeroJudge a015: Transpose matrix
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a015

while True:
  try:
    row, col = input().split() 
    row = int(row)
    col = int(col)
    org = []
    ans = [[0]*row for i in range(col)]
    for i in range(row):
      org = [*org, list(map(int, input().split()))]
    for i in range(row):
      for j in range(col):
        ans[j][i] = org[i][j]
    for i in range(col):
      print(*ans[i])
  except EOFError:
    break
      
