countries = ['USA', 'Great Britain', 'China']
capitals = ['Washington', 'London', 'Beijing']

mydict = dict(zip(countries, capitals))
# print(mydict)

print('-' * 43)
for k, v in mydict.items():
    print(f'|{k:^20}|{v:^20}|')
print('-' * 43)


for country in 'Great Britain', 'Zimbabwe':
    capital = mydict.get(country, 'фиг знает')
    print(f'{capital} is the capital of {country}')

