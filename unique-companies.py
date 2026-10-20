import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print(df['Company'].nunique())
