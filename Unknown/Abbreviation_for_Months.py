# Print the abbreviation for entered month

months = 'JanFebMarAprMayJunJulAugSepOctNovDoc'
n = int(input('Enter a month in numbers:'))
print('The abbreviation for the month is', months[3*n-3:3*n]+'.')
