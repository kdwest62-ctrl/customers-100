import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
domains = df['Email'].str.split('@').str[1]
domain_counts = domains.value_counts().head(10)
print(domain_counts)
