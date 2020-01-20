# read write execute

files = [
    {'name': 'doc.doc', 'actions': 'rwx'},
    {'name': 'run.exe', 'actions': 'x'},
    {'name': 'command.com', 'actions': 'r'}
]

for i, f in enumerate(files):
    print(i, f['name'])

num = int(input('введите номер файла: '))
file = files[num]
print('Вы выбрали', file['name'])

action = input('введите действие (r/w/x): ')

if action in file['actions']:
    print('Запрос подтвержден')
else:
    print('Запрос отклонен')