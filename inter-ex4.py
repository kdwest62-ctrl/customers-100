import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
column_data = df['Last Name'].tolist()

last_names = tuple(set(column_data))

for last_name in last_names:
    count = 0
    for data in column_data:
        if last_name == data:
            count += 1
    if count > 1:
        print(last_name)
