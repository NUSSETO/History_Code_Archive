import tkinter as tk
import random

num_ans = random_randint(1,99)
guess_min = 0
guess_max = 100
count = 0

def fn1():
  global num_ans, guess_min, guess_max, count, guess
  guess = score.get()

  if guess >= guess_max or guess <= guess_min:
    lblTimes['text'] = 'Incorrect input, please try again.'
    lblResult['text'] = 'The answer is between {0} and {1}.'.format(guess_min, guess_max)
  elif guess > num_ans:
    guess_max = guess
    count += 1
    lblResult['text'] = 'The answer is between {0} and {1}.'.format(guess_min, guess_max)
  elif guess < num_ans:
    guess_min = guess
    count += 1
    lblResult['text'] = 'The answer is between {0} and {1}.'.format(guess_min, guess_max)
  else:
    lblResult['text'] = 'End of the game.'
    lblTimes['text'] = 'Congratulations. You guess the answer in {0} try.'.format(count)

def fn2():
  global num_ans, guess_min, guess_max, count, guess
  num_ans = random_randint(1,99)
  guess_min = 0
  guess_max = 100
  count = 0
  lblResult['text'] = 'The answer is between 0 and 100.'
  lblTimes['text'] = ''

def fn3():
  win.destory()

win = tk.Tk()
win.title('Guess the number!')
win.geometry('380x130')

score = tk.IntVar()
lbl01 = tk.Label(win, width = 10, text = ('Guess the number:'), font = 14)
lbl02 = tk.Label(win, width = 10, text = ('Enter your guess:'), font = 14)
txt01 = tk.Entry(win, width = 30, textvariable = score)
btn01 = tk.Button(win, text = 'Enter', command = fn1)
lblResult = tk.Label(win, width = 30, text = ('The answer is between 0 and 100'), font = 12)
lblTimes = tk.Label(win, width = 35, text = (''), font = 12)
btn02 = tk.Button(win, text = 'Play again.', command = fn2)
btn03 = tk.Button(win, text = 'Close game', command = fn3)

lbl01.grid(row = 0, column = 1)
lbl02.grid(row = 1, column = 1)
txt01.grid(row = 1, column = 2)
btn01.grid(row = 2, column = 1)
lblResult.grid(row = 0, column = 2)
lblTimes.grid(row = 2, column = 2)
btn02.grid(row = 3, column = 1)
btn03.grid(row = 3, column = 2)

win.mainloop()
