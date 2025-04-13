# Sum up the string number by number
# The whole code can be replaced with: print(sum(int(i) for i in input()))

num_str = input()
num_sum = 0

for i in num_str:
  j = int(i)
  num_sum += j
  
print(num_sum)
