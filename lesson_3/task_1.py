def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Вы пытаетесь разделить на 0')
        return


a, b = (int(digit) for digit in input('Введите 2 числа через пробел: ').split())
print(divider(a, b))
