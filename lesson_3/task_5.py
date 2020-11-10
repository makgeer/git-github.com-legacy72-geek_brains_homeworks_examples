def my_func():
    digits = []
    while True:
        input_str = input('Введите числа через пробел: ')
        new_digits = input_str.split()
        for digit in new_digits:
            if digit == 'q':
                print(sum(digits))
                return
            digits.append(int(digit))
        print(sum(digits))


my_func()
