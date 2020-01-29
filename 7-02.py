# CSV - comma separated values

import csv

FILE = 'data.csv'

with open(FILE, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print('Чтение завершено')