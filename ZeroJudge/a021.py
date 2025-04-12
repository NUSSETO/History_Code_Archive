# ZeroJudge a021: Big number calculation
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a021

a, b, c = input().split()
a = int(a)
c = int(c)

if b == '+':
  outcome = a + c
elif b == '-':
  outcome = a - c
elif b == '*':
  outcome = a*c
elif b == '/':
  outcome = a//c
else:
  print('Incorrect format')
  
print(outcome)
