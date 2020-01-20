# import os
#
# if not os.path.exists('dir'):
#     os.mkdir('data')

import random

rows = 1000

with open('data/d.dat', 'w', encoding='utf-8') as f:
    for i in range(rows):
        # f.write(str(i + 1) + '\n')
        # f.write(f'line # {i + 1}\n')
        val = round(random.random() * 100, 3)
        f.write(f'value = {val}\n')
