import pandas as pd

df = pd.read_csv('1991-2021rates.csv')

print(df)

['year', 'unemployment rate']

small_df = df[['year','unemployment rate']]

print(small_df.head())