import csv
from faker import Faker
import random

fake = Faker()

FILE = 'fake.csv'

fields = ['name', 'email', 'phone', 'job', 'company', 'salary']

with open(FILE, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for i in range(100):
        row = [
            fake.name(),
            fake.email(),
            fake.phone_number(),
            fake.job(),
            fake.company(),
            round(random.random() * 10000, 2)
        ]
        # print(row)
        writer.writerow(dict(zip(fields, row)))
