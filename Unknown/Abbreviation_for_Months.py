# Print the abbreviation for entered month

months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
n = int(input('Enter a month in numbers:'))
if 1 <= n & n <= 12:
  print('The abbreviation for the month is', months[3*n-3:3*n]+'.')
else:
  print('Error')
