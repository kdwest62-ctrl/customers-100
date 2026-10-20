import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
duplicate_lastnames = df['Last Name'].value_counts()
duplicate_lastnames = duplicate_lastnames[duplicate_lastnames > 1]
print(duplicate_lastnames)
