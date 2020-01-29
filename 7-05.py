import csv

FILE = 'fake.csv'
fields = ['name', 'email', 'phone', 'job', 'company', 'salary']
data = []

with open(FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(dict(row))
        data.append(dict(row))

print('Чтение завершено')

jobs = [d.get('job') for d in data]
for i, j in enumerate(sorted(jobs), start=1):
    print(i, j)