import pandas as pd

series_input = pd.Series(map(int, input().split()))

print(f'Average:{series_input.mean()}')
print(f'Median:{series_input.median()}')
print(f'Mode:{series_input.mode()}')
print(f'Standard deviation:{series_input.std()}')
