import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
column_data = df['Customer Id'].tolist()

length = []
alpha_num = []
for item in column_data:
    length.append(len(item))
    alpha_num.append(item.isalnum())

print(f"All same length? {len(set(length)) == 1}")
print(f"All alphanumeric? {len(set(alpha_num)) == 1}")
