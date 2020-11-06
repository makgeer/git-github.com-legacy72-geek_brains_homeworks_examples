products = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]


index = 4

res = {
    'название': set(),
    'цена': set(),
    'количество': set(),
    'eд': set(),
}

while True:
    menu = int(input('1 - Добавить продукт\n2 - Посмотреть аналитику\n0 - выход\n'))
    if menu == 0:
        break
    elif menu == 1:
        name, price, count, unit = input('Введите через пробел название, цену, кол-во, единицу измерения: ').split()
        products.append((
            index,
            {
                'название': name,
                'цена': float(price),
                'количество': int(count),
                'eд': unit,
            }
        ))
        index += 1
    elif menu == 2:
        for product in products:
            res['название'].add(product[1]['название'])
            res['цена'].add(product[1]['цена'])
            res['количество'].add(product[1]['количество'])
            res['eд'].add(product[1]['eд'])
        print(res)
    else:
        continue
