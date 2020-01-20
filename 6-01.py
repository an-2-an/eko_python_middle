# читаем файлик

with open('text.txt', 'r', encoding='utf-8') as f:
    # data = f.read()
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line.strip())


