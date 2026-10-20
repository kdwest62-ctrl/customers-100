import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print(df['Country'].value_counts().to_string())
