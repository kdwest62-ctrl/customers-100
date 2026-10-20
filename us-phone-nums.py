import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
us_format_phones = df['Phone 1'].str.startswith('+1').sum()
print(f"Phone numbers in US format: {us_format_phones}")
