athlets = [
    {'name': 'Benson', 'results': [220, 210, 200]},
    {'name': 'Johnson', 'results': [190, 205, 220]},
    {'name': 'Harrison', 'results': [185, 215, 205]},
]


for athlet in athlets:
    athlet['avg'] = round(sum(athlet['results']) / 3, 1)
    print(f"{athlet['name']} --> {athlet['avg']}")

print()

for a in sorted(athlets, key=lambda x: x['avg']):
    print(a['name'], a['avg'])



