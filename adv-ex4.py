import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])
earliest = df["Subscription Date"].min()
latest = df["Subscription Date"].max()
print(f"Earliest date: {earliest}")
print(f"Latest date: {latest}")
