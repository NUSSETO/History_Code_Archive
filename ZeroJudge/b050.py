# ZeroJudge b050: Sets operations
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=b050

# I use a improve version of inserting letter, and f-string.
import string

def letter_label(n):
  result = []
  while n >= 0:
    result.append(string.ascii_uppercase[n%26])
    n = n//26 - 1
  return ''.join(reversed(result))

num_set = int(input())
case_indicator = 1

while n != 0: 
  print(f'Test Case {case_indicator}:')
  case_indicator += 1
  list_set = [] # list where sets are stored

  for i in range(num_set):
    list_set.append(input())
    print(f'{letter_label(i)}: {{{list_set[i]}}}')

  # Union
  for i in range(num_set):
    fix_set_union = set(list_set[i])
    for j in range(i + 1, num_set):
      change_set_union = set(list_set[j])
      union_set = fix_set_union.union(change_set_union)
      print(f'{letter_label(i)}+{letter_label(j)}: {{{''.join(sorted(union_set))}}}')

  # Intersection
  for i in range(num_set):
    fix_set_intersection = set(list_set[i])
    for j in range(i + 1, num_set):
      change_set_intersection = set(list_set[j])
      intersection_set = fix_set_intersection.intersection(change_set_intersection)
      print(f'{letter_label(i)}*{letter_label(j)}: {{{''.join(sorted(intersection_set))}}}')

  # Difference
  for i in range(num_set):
    fix_set_difference = set(list_set[i])
    for j in range(num_set):
      if i != j:
        change_set_difference = set(list_set[j])
        difference_set = fix_set_difference.difference(change_set_difference)
        print(f'{letter_label(i)}-{letter_label(j)}: {{{''.join(sorted(difference_set))}}}')

  # Contain
  for i in range(num_set):
    fix_set_contain = set(list_set[i])
    for j in range(num_set):
      if i != j:
        change_set_contain = set(list_set[j])
        if fix_set_contain.issuperset(change_set_contain):
          print(f'{letter_label(i)} contains {letter_label(j)}')
        else:
          print(f'{letter_label(i)} does not contain {letter_label(j)}')

  num_set = int(input()) # Enter 0 to stop 
