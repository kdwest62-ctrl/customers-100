import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
data1 = df["First Name"].value_counts()
data2 = df["Last Name"].value_counts()
common_first = data1[data1 > 1]
common_last = data2[data2 > 1]
print(common_first)
print('-' * 8)
print(common_last)
