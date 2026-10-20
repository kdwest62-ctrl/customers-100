import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])
by_year = df['Subscription Date'].dt.year.value_counts()
by_month = df['Subscription Date'].dt.month.value_counts()
print(by_year)
print(by_month)
