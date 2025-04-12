# ZeroJudge a022: Palindrome
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a022

n = input()
m = n[-1::-1] # Reverse the input

if n == m:
  print('Yes')
else:
  print('No')
