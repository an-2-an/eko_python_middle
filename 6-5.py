from faker import Faker
fake = Faker('ru_RU')

rows = 1000

with open('data/fake.txt', 'w', encoding='utf-8') as f:
    for i in range(rows):
        name = fake.name()
        country = fake.country()
        email = fake.email()
        phone = fake.phone_number()
        f.write(f'{name},{country},{email},{phone}\n')

