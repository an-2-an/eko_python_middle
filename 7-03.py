import csv

FILE = 'data1.csv'
fields = ['surname', 'name', 'age']
data = []

with open(FILE, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        data.append(dict(zip(fields, row)))

print('Чтение завершено')

for d in data:
    print(d)

ages = [int(d.get('age')) for d in data]
print(ages)
