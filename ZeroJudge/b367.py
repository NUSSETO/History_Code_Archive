# ZeroJudge b367: Upside down
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=b367

num_data = int(input())

for i in range(num_data):
  list_original = []
  list_flipped = []

  length, width = map(int, input().split()) # Don't really need width in this case

  for j in range(length):
    list_original.append(list(map(int, input().split())))
    list_flipped.append(list(list_original[j]))

  list_flipped.reverse()
  for j in range(length):
    list_flipped[j].reverse()

  if list_original == list_flipped:
    print('Go forward.')
  else:
    print('Keep defending.')
  
