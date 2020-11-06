earnings = float(input('Введите значение выручки: '))
outgoings = float(input('Введите значение издержек: '))

if earnings > outgoings:
    profit = earnings - outgoings
    print(f'Фирма работает в плюс, рентабельность выручки: {profit / earnings:.2f}')
    count_workers = int(input('Введите кол-во сотрудников: '))
    print(f'Прибыль фирмы на одного сотрудника: {profit / count_workers}')
elif earnings < outgoings:
    print('Фирма работает в минус')
else:
    print('Доходы и расходы равны')
