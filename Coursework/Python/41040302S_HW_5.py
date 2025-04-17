import pandas as pd

df = pd.read_csv('scores.csv')

cols = ['Chinese', 'English', 'Math', 'Physics', 'Chemistry']

score_sum = df[cols].sum(axis = 1)
score_mean = df[cols].mean(axis = 1)

df['Total'] = score_sum
df['Average'] = score_mean

df = df.sort_value(by = 'Total', ascending = False)
df['Rank'] = ['{:02d}'.format(i) for i in range(1, 51)]
df = df.sort_value(by = 'Student ID', ascending = True)

print(df)
print(f'Average score for each subjects:{df[cols].mean()}')
print(f'Standard deviation for each subjects:{df[cols].std()}')
print(f'Median score for each subjects:{df[cols].median()}')
