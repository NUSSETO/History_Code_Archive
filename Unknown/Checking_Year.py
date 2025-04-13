# Check the year is common year ot leap year

year = int(input()) # Only in A.D.

if year < 0:
  print('Error')

if (year%400 == 0)|((year%4 == 0)&(year%100 != 0)):
  print('Leap year')
else:
  print('Common year')
