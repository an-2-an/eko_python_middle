lines = [
    'О как же я люблю вас,',
    'прекрасное созданье,',
    'люблю ваш голос нежный',
    'и этот дивный взгляд'
]

with open('thefolder/text1.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line + '\n')
    print('Запись завершена')
