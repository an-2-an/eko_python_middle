s = 0.0

with open('data/d.dat', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        # print(line.strip())
        # value = float(line.strip().replace('value = ', ''))
        value = float(line.strip().split(' = ')[1])
        # print(value)
        s += value

s = round(s, 3)
print(f'S = {s}')

