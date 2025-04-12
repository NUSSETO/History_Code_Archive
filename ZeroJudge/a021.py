# ZeroJudge a021: Big number calculation
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a021

# Read the input: number 1, operator, number 2
a, b, c = input().split()
a = int(a)
c = int(c)

# Perform operation based on the operator
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
