# Check the year is common year ot leap year
# Might as well just make this a function.

year = int(input('Enter a year (A.D.)')) 

if year < 0:
  print('Error')

if (year%400 == 0)|((year%4 == 0)&(year%100 != 0)):
  print('Leap year')
else:
  print('Common year')
