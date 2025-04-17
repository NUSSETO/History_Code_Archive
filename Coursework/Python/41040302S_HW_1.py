age = int(input('How old are you?'))

if age <= 0 or age > 123: # Since oldest person ever is under 123 years old.
  print('Incorrect input.')
elif age <= 5:
  print('No need for tickets.')
elif age <= 11:
  print('Child tickets.')
elif age <= 17:
  print('Teenager tickets.')
elif age <= 59:
  print('Adult tickets.')
else:
  print('Elderly tickets.')
