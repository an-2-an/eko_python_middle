# json

staff = {
    'Иванов': 2000,
    'Петрова': 2100,
    'Семенов': 1900,
    'Харина': 1950
}

# суммарная ЗП
print(staff.values())
s = sum(staff.values())
print(f'суммарная ЗП: {s}')

# максимальная ЗП
max_salary = max(staff.values())
print(f'максимальная ЗП: {max_salary}')
ind = list(staff.values()).index(max_salary)
rich = list(staff.keys())[ind]
print(f'...и ее счастливый обладатель: {rich}')



