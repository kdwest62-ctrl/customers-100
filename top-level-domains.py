import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
tld = df['Email'].str.split('.').str[1]
print(tld.value_counts())
