#dict

car = {
    'mark': 'BMW',
    'size': 3000,
    'price': 120.0,
    'auto': False
}

print(car)
print(type(car))

# print(car['size'])

car['plate'] = 'AR1122EE'

for key in car.keys():
    print(key, car[key])

