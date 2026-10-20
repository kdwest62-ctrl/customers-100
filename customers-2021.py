import pandas as pd

path = input("Path: ")
df = pd.read_csv(path)
df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])
customers_2021 = df[df['Subscription Date'].dt.year == 2021]
print(customers_2021.to_string())
