import random

num_ans = random.randint(1,99)

guess = int(input('Enter number between 0 and 100:'))
guess_min = 0
guess_max = 100

while guess != num_ans:
  if guess >= guess_max or guess <= guess_min:
    print('Incorrect input.')
    print('Please try again:')
  elif guess_min < guess < num_ans:
    guess_min = guess
    guess = int(input(f'Enter number between {guess_min} and {guess_max}'))
  elif num_ans < guess < guess_max:
    guess_max = guess
    guess = int(input(f'Enter number between {guess_min} and {guess_max}'))

print('Correct answer!')
