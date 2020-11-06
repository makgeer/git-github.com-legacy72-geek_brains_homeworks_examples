a = float(int(input('Введите расстояние в км, сколько пробежал спортсмен в первый день: ')))
b = float(int(input('Введите расстояние в км, сколько нужно достичь спортсмену: ')))

counter = 1
while a <= b:
    print(f'{counter} день: {round(a, 2)} км.')
    a *= 1.1
    counter += 1

print(f'{counter} день: {round(a, 2)} км.')
print(f'Спортсмен пробежит не менее {b} км на {counter} день')
