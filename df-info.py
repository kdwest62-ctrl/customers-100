import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
print(df.shape)
print(df.columns)
print(df.dtypes)
