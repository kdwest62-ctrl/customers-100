import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)

column_data = []
for item in df['Website'].tolist():
    data = item.split('.')
    column_data.append(data[-1])

domains = []
for data in column_data:
    if data not in domains:
        domains.append(data)

scores = []
for domain in domains:
    count = 0
    for data in column_data:
        if data == domain:
            count += 1
    scores.append(count)

domain_scores = dict(zip(domains, scores))
for domain, score in domain_scores.items():
    print(f"{domain}: {score}")
